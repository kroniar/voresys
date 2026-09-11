# Authorization

Implemented roles are organization-scoped: Admin, Maintainer, Developer, Viewer. Membership connects a user to one organization and one role. Roles own the initial `organization.*`, `user.*`, and `role.*` permission codes. Platform administration is deliberately not an organization role and is not implemented.
