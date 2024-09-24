#!/bin/bash

set -e

echo "Running custom deployment script..."

pip install -r requirements.txt

python manage.py collectstatic --noinput

echo "Deployment script finished successfully."
