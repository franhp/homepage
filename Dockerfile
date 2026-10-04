FROM docker.io/library/python:3.14 AS backend

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

RUN apt-get -y update && \
    apt-get -y upgrade && \
    apt-get -y install \
        binutils \
        libproj-dev \
        gdal-bin \
        libsqlite3-mod-spatialite

COPY --from=ghcr.io/astral-sh/uv:0.11.33 /uv /uvx /bin/
ENV UV_PROJECT_ENVIRONMENT=/opt/venv
ENV UV_PYTHON_DOWNLOADS=never
ENV UV_LINK_MODE=copy
ENV PATH="/opt/venv/bin:$PATH"

WORKDIR /usr/src/app/homepage/backend
COPY backend/pyproject.toml backend/uv.lock ./
RUN --mount=type=cache,target=/root/.cache/uv uv sync --locked --no-dev --no-install-project

ADD . /usr/src/app/homepage
RUN bash -c "python manage.py out_bookmarks && python manage.py out_wiki && python manage.py out_places && python manage.py out_watched"


FROM docker.io/library/node:26 AS frontend

COPY --from=backend /usr/src/app/homepage/ /usr/src/app/homepage/
WORKDIR /usr/src/app/homepage/frontend
RUN npm i && npm run-script build

FROM docker.io/library/caddy:latest AS static
COPY Caddyfile /etc/caddy/Caddyfile
COPY --from=frontend /usr/src/app/homepage/frontend/build/ /usr/share/caddy/
