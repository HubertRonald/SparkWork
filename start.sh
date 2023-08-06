#!/bin/bash

# autor: @hubertronald

# Available environment variables
# file .env has default environment variables
source $(pwd)/.env


# Create and up detach Service Container
docker-compose build
docker-compose up -d
sleep 10s
docker-compose logs
