# Architecture overview

## Implemented

Verosys is a Django modular monolith backed by PostgreSQL, with a Next.js client and Redis/Celery worker foundation. One deployment serves many organizations.

```text
Next.js → Django API → PostgreSQL
                   → Redis → Celery worker
```

## Planned and future

Repositories, environments, tasks, integrations, security scans, and audit events will be separate organization-owned models. A future Verosys Control Plane is a separate service that may manage instance-wide organization lifecycle and health through APIs; it is not part of this application.
