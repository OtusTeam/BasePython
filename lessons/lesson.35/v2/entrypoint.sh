#!/usr/bin/env bash

echo "Starting db upgrade"
flask db upgrade
echo "OK"

exec "$@"
