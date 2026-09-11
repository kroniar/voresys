from django.contrib.auth.models import User
from django.db import models, transaction
from django.utils.text import slugify


class Organization(models.Model):
    name = models.CharField(max_length=120)
    slug = models.SlugField(max_length=140, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ("name",)

    def __str__(self):
        return self.name

    @classmethod
    @transaction.atomic
    def create_with_administrator(cls, *, username, email, password, name):
        base_slug = slugify(name) or "organization"
        slug, suffix = base_slug, 2
        while cls.objects.filter(slug=slug).exists():
            slug = f"{base_slug}-{suffix}"
            suffix += 1
        user = User.objects.create_user(username=username, email=email, password=password)
        organization = cls.objects.create(name=name, slug=slug)
        permissions = {
            code: Permission.objects.get_or_create(code=code, defaults={"name": code.replace(".", " ").title()})[0]
            for code in DEFAULT_PERMISSIONS
        }
        roles = {}
        for role_name, codes in DEFAULT_ROLES.items():
            role = Role.objects.create(organization=organization, name=role_name)
            role.permissions.set(permissions[code] for code in codes)
            roles[role_name] = role
        Membership.objects.create(user=user, organization=organization, role=roles["Admin"])
        return organization, user


class Permission(models.Model):
    code = models.CharField(max_length=80, unique=True)
    name = models.CharField(max_length=120)

    def __str__(self):
        return self.code


class Role(models.Model):
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE, related_name="roles")
    name = models.CharField(max_length=40)
    permissions = models.ManyToManyField(Permission, related_name="roles", blank=True)

    class Meta:
        constraints = [models.UniqueConstraint(fields=("organization", "name"), name="unique_role_per_organization")]

    def __str__(self):
        return f"{self.organization}: {self.name}"


class Membership(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="memberships")
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE, related_name="memberships")
    role = models.ForeignKey(Role, on_delete=models.PROTECT, related_name="memberships")
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        constraints = [models.UniqueConstraint(fields=("user", "organization"), name="unique_organization_membership")]

    def clean(self):
        if self.role_id and self.organization_id and self.role.organization_id != self.organization_id:
            from django.core.exceptions import ValidationError

            raise ValidationError("Membership role must belong to its organization.")

    def save(self, *args, **kwargs):
        self.full_clean()
        return super().save(*args, **kwargs)


DEFAULT_PERMISSIONS = (
    "organization.read",
    "organization.manage",
    "user.read",
    "user.manage",
    "role.read",
    "role.manage",
)
DEFAULT_ROLES = {
    "Admin": DEFAULT_PERMISSIONS,
    "Maintainer": ("organization.read", "user.read", "user.manage", "role.read"),
    "Developer": ("organization.read", "user.read", "role.read"),
    "Viewer": ("organization.read", "user.read", "role.read"),
}
