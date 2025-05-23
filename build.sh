
#!/usr/bin/env bash
# Install dependencies
pip install -r requirements.txt

# Apply migrations
python manage.py migrate

# Create superuser if it doesn't exist
python - <<'PYCODE'

