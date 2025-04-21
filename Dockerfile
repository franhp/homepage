FROM docker.io/library/python:3.12 as backend

RUN apt-get -y update && \
    apt-get -y upgrade && \
    apt-get -y install \
        binutils \
        libproj-dev \
        gdal-bin \
        libsqlite3-mod-spatialite

ADD backend/requirements.txt /
RUN pip install -r /requirements.txt

RUN mkdir -p /usr/src/app/homepage
ADD . /usr/src/app/homepage

WORKDIR /usr/src/app/homepage/backend
RUN bash -c "python manage.py out_bookmarks && python manage.py out_wiki && python manage.py out_places && python manage.py out_watched"


FROM node:20 as frontend

COPY --from=backend /usr/src/app/homepage/ /usr/src/app/homepage/
WORKDIR /usr/src/app/homepage/frontend
RUN npm i && npm run-script build

FROM caddy:latest as static
COPY --from=frontend /usr/src/app/homepage/frontend/build/ /usr/share/caddy/
