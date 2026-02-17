#!/usr/bin/env bash

set -e

echo "Apply migrations..."
alembic upgrade head
echo "Migrations applied, starting"

exec "$@"
