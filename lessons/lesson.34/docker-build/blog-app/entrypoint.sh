#!/usr/bin/env bash

set -e

echo "Applying migrations..."
alembic upgrade head
echo "Migrations applied."

exec "$@"
