from rest_framework.exceptions import NotFound, PermissionDenied

from .models import Membership, Organization


class OrganizationContextMixin:
    """Resolve an organization only from a membership validated header.

    Future organization-owned views use self.organization and always filter with it.
    """

    organization = None

    def initial(self, request, *args, **kwargs):
        super().initial(request, *args, **kwargs)
        header_id = request.headers.get("X-Organization-ID")
        url_id = kwargs.get("pk")
        if header_id and url_id and str(header_id) != str(url_id):
            raise PermissionDenied("Organization context does not match the requested resource.")
        raw_id = header_id or url_id
        if raw_id:
            try:
                self.organization = Organization.objects.get(pk=raw_id)
            except (Organization.DoesNotExist, ValueError):
                raise NotFound("Organization not found.")
            if not Membership.objects.filter(user=request.user, organization=self.organization).exists():
                raise PermissionDenied("You do not have access to this organization.")

    def require_permission(self, code):
        if not self.organization:
            raise PermissionDenied("An organization context is required.")
        permitted = Membership.objects.filter(
            user=self.request.user, organization=self.organization, role__permissions__code=code
        ).exists()
        if not permitted:
            raise PermissionDenied("Your role does not have this permission.")
