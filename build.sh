#!/usr/bin/env bash
#set -o errexit
#!/bin/bash

echo "Installing dependencies..."
pip install -r requirements.txt

echo "Running collectstatic..."
python manage.py collectstatic --noinput

echo "Running database migrations..."
python manage.py migrate

#pip install -r requirements.txt
#python manage.py collectstatic --no-input
#python manage.py migrate