# ADR 0001: Shared-schema tenancy

**Status: accepted.** Verosys uses one PostgreSQL database and public schema. Every organization-owned record will carry a direct `organization` foreign key. This is the smallest practical starting point, while keeping a later stronger-isolation deployment strategy possible.
