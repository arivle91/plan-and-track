from django.contrib.auth.models import User
from django.core.management import call_command
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'plantrack.settings')
django.setup()

# ⬇️ Импорт перенеси СЮДА — после django.setup()

# Apply migrations
call_command('migrate')

# Create superuser if not exists
if not User.objects.filter(username='admin').exists():
    User.objects.create_superuser('admin', 'admin@example.com', 'adminpass')
    print("✅ Superuser created: admin / adminpass")
else:
    print("ℹ️ Superuser already exists.")
