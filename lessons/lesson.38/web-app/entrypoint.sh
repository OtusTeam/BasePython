#!/usr/bin/env bash

echo "Running migrations"
flask db upgrade

echo "Starting app..."
exec "$@"
