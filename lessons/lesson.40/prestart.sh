#!/usr/bin/env bash

echo Apply migrations...

flask db upgrade

echo migrations ok

exec "$@"
