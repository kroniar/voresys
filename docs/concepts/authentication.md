# Authentication

Implemented: Django hashes passwords; SimpleJWT issues access and refresh tokens at `/api/v1/auth/login/`. Clients use `Authorization: Bearer <access-token>`. Tokens and passwords must never be logged.

The API uses JWT rather than cookie authentication, so CSRF protection is not the authentication mechanism for these endpoints. Browser CORS is explicitly restricted by `CORS_ALLOWED_ORIGINS`; set it to production origins outside development.
