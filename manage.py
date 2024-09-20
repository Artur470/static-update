#!/usr/bin/env python

import os
import sys
from decouple import config  # Добавьте этот импорт

# Вывод переменных окружения для проверки
print(f"DB_NAME: {config('DB_NAME')}")
print(f"DB_USER: {config('DB_USER')}")
print(f"DB_PASSWORD: {config('DB_PASSWORD')}")
print(f"DB_HOST: {config('DB_HOST')}")
print(f"DB_PORT: {config('DB_PORT')}")

# Установите переменную окружения для указания настроек Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")

if __name__ == "__main__":
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)
