from django.contrib.auth.models import User
from rest_framework import serializers

from apps.organizations.models import Membership, Organization


class RegisterSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=150)
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True, min_length=12)
    organization_name = serializers.CharField(max_length=120)

    def validate_username(self, value):
        if User.objects.filter(username=value).exists():
            raise serializers.ValidationError("This username is already in use.")
        return value

    def create(self, validated_data):
        return Organization.create_with_administrator(
            username=validated_data["username"],
            email=validated_data["email"],
            password=validated_data["password"],
            name=validated_data["organization_name"],
        )


class MeSerializer(serializers.ModelSerializer):
    organizations = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = ("id", "username", "email", "organizations")

    def get_organizations(self, user):
        memberships = Membership.objects.filter(user=user).select_related("organization", "role")
        return [
            {"id": m.organization_id, "name": m.organization.name, "slug": m.organization.slug, "role": m.role.name}
            for m in memberships
        ]
