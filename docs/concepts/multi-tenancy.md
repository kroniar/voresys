# Multi-tenancy

## Implemented security invariant

```text
One Verosys deployment → many organizations → many users per organization → organization-scoped resources
```

Every future organization-owned model must directly reference `Organization`. A request resolves `current_user` from JWT and `current_organization` from an `X-Organization-ID` header only after confirming membership. The header itself conveys no authority. Querysets must filter by that resolved organization, and object access must verify both membership and resource ownership.

Workers must accept `organization_id` with their work identifier and resolve that tenant before accessing data. Future audit events must include organization, actor, action, resource, timestamp, and non-sensitive metadata. Never store secrets, tokens, or credentials in audit metadata.

## Planned

Organization selection will become a full switcher for users with multiple memberships. Database-per-tenant and schema-per-tenant are not implemented.
