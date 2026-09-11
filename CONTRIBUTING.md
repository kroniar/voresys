# Contributing

Keep changes small, tested, and explicit. New organization-owned models must include a direct `ForeignKey(Organization)` and every API queryset must be scoped through a membership-validated organization context. Never log credentials, tokens, API keys, or secret values.

Run backend tests with `docker compose run --rm backend python manage.py test`, frontend checks with `docker compose run --rm frontend npm run typecheck`, and Helm validation with `helm lint deploy/helm/verosys`.
