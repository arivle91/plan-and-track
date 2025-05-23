#!/usr/bin/env bash
#set -o errexit
#!/bin/bash

# echo "Installing dependencies..."
# pip install -r requirements.txt

# echo "Running collectstatic..."
# python manage.py collectstatic --noinput

# echo "Running database migrations..."
# python manage.py migrate

#pip install -r requirements.txt
#python manage.py collectstatic --no-input
#python manage.py migrate

#!/usr/bin/env bash
# Install dependencies
pip install -r requirements.txt

# Apply migrations
python manage.py migrate

# Create superuser if it doesn't exist
python - <<EOF
from django.contrib.auth.models import User
if not User.objects.filter(username='admin').exists():
    User.objects.create_superuser('admin', 'admin@example.com', 'adminpass')
    print("🏆 Superuser created")
else:
    print("ℹ️ Superuser already exists")
EOF
