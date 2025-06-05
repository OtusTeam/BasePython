#!/usr/bin/env bash

set -e

echo "Apply alembic migrations"
alembic upgrade head
echo "Successfully applied migrations."

exec "$@"
