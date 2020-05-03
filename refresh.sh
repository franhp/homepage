#!/bin/bash

docker-compose build
docker-compose run --rm frontend npm run clean
docker-compose run --rm backend python manage.py migrate
docker-compose run --rm backend
docker-compose run --rm frontend