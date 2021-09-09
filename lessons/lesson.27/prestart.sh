#!/usr/bin/env sh

echo "Run migrations"
flask db upgrade
