#!/usr/bin/env bash

set -e

echo "Applying alembic migrations..."
alembic upgrade head
echo "Migrations applied."

exec "$@"
