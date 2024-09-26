#!/usr/bin/env bash

echo "Starting"

flask db upgrade

echo "OK"

exec "$@"
