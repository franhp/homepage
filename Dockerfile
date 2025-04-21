FROM docker.io/library/python:3.13 AS backend

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

RUN apt-get -y update && \
    apt-get -y upgrade && \
    apt-get -y install \
        binutils \
        libproj-dev \
        gdal-bin \
        libsqlite3-mod-spatialite

ADD backend/Pipfile* /
RUN python -m pip install --upgrade pip && pip install pipenv && pipenv install --dev --system --deploy

RUN mkdir -p /usr/src/app/homepage
ADD . /usr/src/app/homepage

WORKDIR /usr/src/app/homepage/backend
RUN bash -c "python manage.py out_bookmarks && python manage.py out_wiki && python manage.py out_places && python manage.py out_watched"


FROM docker.io/library/node:23 AS frontend

COPY --from=backend /usr/src/app/homepage/ /usr/src/app/homepage/
WORKDIR /usr/src/app/homepage/frontend
RUN npm i && npm run-script build

FROM docker.io/library/caddy:latest AS static
COPY --from=frontend /usr/src/app/homepage/frontend/build/ /usr/share/caddy/
