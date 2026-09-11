from rest_framework import serializers

from .models import Organization


class OrganizationSerializer(serializers.ModelSerializer):
    role = serializers.SerializerMethodField()

    class Meta:
        model = Organization
        fields = ("id", "name", "slug", "role", "created_at")

    def get_role(self, organization):
        return organization.memberships.get(user=self.context["request"].user).role.name
