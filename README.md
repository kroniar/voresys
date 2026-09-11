# Verosys

Verosys is an open-source, multi-tenant foundation for a future SRE and platform engineering control plane. This release intentionally implements tenancy, authentication, authorization, deployment scaffolding, and a minimal product shell—rather than future operational integrations.

## Run locally

```bash
cp .env.example .env
docker compose up --build
```

Open http://localhost:3000, register an organization, then sign in. The API is at http://localhost:8000/api/v1/ and health is available at `/api/v1/health/`.

## What is implemented

- Django + DRF API with hashed Django passwords and SimpleJWT tokens
- Shared PostgreSQL schema with explicit organization, membership, role, and permission models
- Membership-validated organization context (`X-Organization-ID`) for future organization-owned API resources
- Organization-scoped roles and permission foundation
- Next.js App Router shell with auth, organization header, sidebar, overview, and future-page placeholders
- Redis/Celery worker foundation whose future task signature includes `organization_id`
- Docker Compose, Helm scaffolding, tests, and contributor documentation

## Security model

An organization ID is never trusted on its own: it is resolved only after checking the authenticated user's membership. Future organization-owned querysets must filter against that resolved organization; see [multi-tenancy documentation](docs/concepts/multi-tenancy.md).

## Status

Implemented: platform foundation only. Planned/future: repositories, environments, AI tasks, integrations, scans, audit events, and a separate platform control plane.
