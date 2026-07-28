# Afrekaskrá FRÍ

## How-to:
0. Install Python 3.12 (same version as the backend Docker image, see `backend/Dockerfile`).
1. sudo apt install libpq-dev unixodbc-dev libsqliteodbc tdsodbc python3-dev npm git build-essentials
2. git clone
3. cd frontend && npm install
4. npm run build
5. python3 -m venv env
6. source env/bin/activate
7. pip install -r backend/requirements.txt
8. Set the environment variables listed below.
9. cd backend && python manage.py runserver

## Environment variables

Required — the backend will not start without these:

| Variable | Description |
| --- | --- |
| `SIF_SECRET_KEY` | Django secret key. |
| `SIF_DB_NAME` | MS-SQL database name. |
| `SIF_DB_HOST` | MS-SQL host. |
| `SIF_DB_PORT` | MS-SQL port. |
| `SIF_DB_USER` | MS-SQL user. |
| `SIF_DB_PASSWORD` | MS-SQL password. |

Optional:

| Variable | Default | Description |
| --- | --- | --- |
| `SIF_IN_PROD` | `0` | Set to `1` to turn `DEBUG` off and enable the production Redis cache. |
| `SIF_ON_RENDER` | unset | Set by Render. Forces HTTPS and enables the Redis cache in dev deploys. |
| `REDIS_URL` | unset | Redis connection string, supplied automatically by Render. Only read when `SIF_IN_PROD=1` or `SIF_ON_RENDER` is set; otherwise a dummy cache is used. The older name `SIF_REDIS_URL` is still accepted. |

## Python version

The pinned versions in `backend/requirements.txt` need wheels for whichever
Python you run locally. Production runs Python 3.12; if you use a newer
interpreter, some pins may have no matching wheel and `pip install` will fail
or fall back to building from source.
