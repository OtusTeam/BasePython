#!/usr/bin/env bash

echo "Running prestart, run migrations"

flask db upgrade
