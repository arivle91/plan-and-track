from django.contrib.auth.models import User
from django.core.management import call_command
import os
import django

# Set the Django settings module
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'plantrack.settings')

# Setup Django
django.setup()

# Now import models and call_command AFTER setup

# Run migrations
call_command('migrate')

# Create a superuser if not already exists
if not User.objects.filter(username='admin').exists():
    User.objects.create_superuser('admin', 'admin@example.com', 'adminpass')
    print("✅ Superuser created: admin / adminpass")
else:
    print("ℹ️ Superuser already exists.")
