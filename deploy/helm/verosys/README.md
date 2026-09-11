# Verosys Helm chart

This chart deploys frontend, backend, and worker workloads. PostgreSQL and Redis are external/managed dependencies; set their connection values in `values.yaml` or a secure values file.

For production, supply `secrets.djangoSecretKey` and `secrets.postgresPassword` through a secret values mechanism. Enable ingress only after setting a real host and TLS policy.
