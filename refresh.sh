#!/bin/bash

docker-compose build
docker-compose run --rm frontend npm run clean
docker-compose run --rm backend
docker-compose run --rm frontend