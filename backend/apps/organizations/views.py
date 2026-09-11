from rest_framework import generics

from .models import Organization
from .permissions import OrganizationContextMixin
from .serializers import OrganizationSerializer


class OrganizationListView(generics.ListAPIView):
    serializer_class = OrganizationSerializer

    def get_queryset(self):
        return Organization.objects.filter(memberships__user=self.request.user).distinct()


class OrganizationDetailView(OrganizationContextMixin, generics.RetrieveAPIView):
    serializer_class = OrganizationSerializer
    lookup_url_kwarg = "pk"

    def get_queryset(self):
        return Organization.objects.filter(memberships__user=self.request.user).distinct()
