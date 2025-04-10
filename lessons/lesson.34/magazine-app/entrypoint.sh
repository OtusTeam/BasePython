#!/usr/bin/env bash

echo "Apply migrations"

alembic upgrade head

echo "Migrations OK"

exec "$@"
