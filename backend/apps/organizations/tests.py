from rest_framework.test import APITestCase
from rest_framework_simplejwt.tokens import RefreshToken

from .models import Organization


class TenantIsolationTests(APITestCase):
    def setUp(self):
        self.org_a, self.user_a = Organization.create_with_administrator(
            username="user-a", email="a@example.com", password="sufficient-password", name="Acme"
        )
        self.org_b, self.user_b = Organization.create_with_administrator(
            username="user-b", email="b@example.com", password="sufficient-password", name="ExampleCorp"
        )

    def authenticate(self, user):
        self.client.credentials(HTTP_AUTHORIZATION=f"Bearer {RefreshToken.for_user(user).access_token}")

    def test_registration_creates_organization_membership_and_admin_role(self):
        membership = self.user_a.memberships.get(organization=self.org_a)
        self.assertEqual(membership.role.name, "Admin")
        self.assertTrue(membership.role.permissions.filter(code="organization.manage").exists())

    def test_registration_endpoint_creates_tenant(self):
        response = self.client.post(
            "/api/v1/auth/register/",
            {
                "username": "new-user",
                "email": "new@example.com",
                "password": "sufficient-password",
                "organization_name": "New Org",
            },
        )
        self.assertEqual(response.status_code, 201)
        self.assertTrue(response.data["organization"]["id"])

    def test_user_cannot_access_another_organization(self):
        self.authenticate(self.user_a)
        response = self.client.get(f"/api/v1/organizations/{self.org_b.id}/", HTTP_X_ORGANIZATION_ID=str(self.org_b.id))
        self.assertEqual(response.status_code, 403)

    def test_organization_list_is_scoped_to_membership(self):
        self.authenticate(self.user_a)
        response = self.client.get("/api/v1/organizations/")
        self.assertEqual([item["id"] for item in response.data], [self.org_a.id])

    def test_jwt_login_and_authenticated_me(self):
        response = self.client.post("/api/v1/auth/login/", {"username": "user-a", "password": "sufficient-password"})
        self.assertEqual(response.status_code, 200)
        self.client.credentials(HTTP_AUTHORIZATION=f"Bearer {response.data['access']}")
        self.assertEqual(self.client.get("/api/v1/auth/me/").status_code, 200)
