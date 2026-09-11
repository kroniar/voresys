from django.urls import path

from .views import OrganizationDetailView, OrganizationListView

urlpatterns = [path("", OrganizationListView.as_view()), path("<int:pk>/", OrganizationDetailView.as_view())]
