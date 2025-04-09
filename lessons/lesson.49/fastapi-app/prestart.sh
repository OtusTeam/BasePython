#!/usr/bin/env bash

echo "Applying migrations..."
alembic upgrade head
echo "Applied migrations!"

exec "$@"
