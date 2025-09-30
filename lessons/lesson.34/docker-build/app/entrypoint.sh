#!/usr/bin/env bash

set -e

echo "Applying migrations..."
alembic upgrade head
echo "Done migrations, starting app..."

exec "$@"
