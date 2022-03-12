#!/usr/bin/env bash

set -e

echo "Apply migrations"

flask db upgrade

echo "migrations ok"

exec "$@"

# prestart.sh echo hello world

# Apply migrations
# upgrade..
# migrations ok
# hello world
