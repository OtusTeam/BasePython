#!/bin/bash
set -e

echo "Run migrations"
flask db upgrade

exec "$@"
