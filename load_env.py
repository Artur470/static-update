from dotenv import load_dotenv
import os

# Загрузите переменные окружения из файла .env
load_dotenv()

def print_env_var(name):
    value = os.getenv(name)
    try:
        print(f"{name}: {value}")
    except UnicodeDecodeError as e:
        print(f"Error reading {name}: {e}")

if __name__ == "__main__":
    print_env_var('DB_NAME')
    print_env_var('DB_USER')
    print_env_var('DB_PASSWORD')
    print_env_var('DB_HOST')
    print_env_var('DB_PORT')
