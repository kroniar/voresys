# Development setup

Copy `.env.example` to `.env`, choose real development secrets, and run `docker compose up --build`. No local PostgreSQL, Redis, Node.js, or Python installation is required.

Run checks:

```bash
docker compose run --rm backend python manage.py test
docker compose run --rm frontend npm run lint
docker compose run --rm frontend npm run typecheck
docker compose run --rm frontend npm run build
helm lint deploy/helm/verosys
```
