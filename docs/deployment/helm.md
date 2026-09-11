# Helm deployment

The chart at `deploy/helm/verosys` deploys frontend, backend, and worker workloads only. Use managed/external PostgreSQL and Redis, provide environment values and secrets through your deployment system, and configure ingress/TLS for the target cluster.
