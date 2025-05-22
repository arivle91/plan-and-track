import os
import django


def main():
    # 1) Устанавливаем DJANGO_SETTINGS_MODULE
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'plantrack.settings')
    # 2) Загружаем конфигурацию Django
    django.setup()

    # 3) Только после setup — импортируем management и модели
    from django.core.management import call_command
    from django.contrib.auth.models import User

    # 4) Применяем миграции
    call_command('migrate')

    # 5) Создаём суперпользователя, если ещё нет
    if not User.objects.filter(username='admin').exists():
        User.objects.create_superuser(
            'admin', 'admin@example.com', 'adminpass')
        print("✅ Superuser created: admin / adminpass")
    else:
        print("ℹ️ Superuser already exists.")


if __name__ == '__main__':
    main()
