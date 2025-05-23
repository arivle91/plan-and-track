#!/usr/bin/env bash
# Install dependencies
pip install -r requirements.txt

# Apply migrations
python manage.py migrate

# Create superuser if it doesn't exist
python - << 'PYCODE'
from django.contrib.auth.models import User

if not User.objects.filter(username='admin').exists():
    User.objects.create_superuser('admin', 'admin@example.com', 'adminpass')
    print("🏆 Superuser created")
else:
    print("ℹ️ Superuser already exists")
PYCODE