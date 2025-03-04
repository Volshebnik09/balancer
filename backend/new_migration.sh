#!/bin/sh

NAME=$1

docker compose exec backend python -m alembic revision --autogenerate -m $NAME
