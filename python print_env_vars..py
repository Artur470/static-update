import os
from dotenv import load_dotenv

# Загрузка переменных окружения из файла .env
load_dotenv()

def print_env_vars():
    env_vars = [
        'SECRET_KEY',
        'DEBUG',
        'DB_NAME',
        'DB_USER',
        'DB_PASSWORD',
        'DB_HOST',
        'DB_PORT'
    ]
    for var in env_vars:
        value = os.getenv(var)
        print(f"{var}: {value} (Type: {type(value)})")

if __name__ == "__main__":
    print_env_vars()
