from dotenv import load_dotenv, find_dotenv
import os

# Попытка найти файл .env
dotenv_path = find_dotenv()
print(f"Путь к .env: {dotenv_path}")

# Загружаем переменные окружения из .env
load_dotenv(dotenv_path=dotenv_path)

# Выводим переменные окружения
print("SECRET_KEY:", os.getenv('SECRET_KEY'))
print("DEBUG:", os.getenv('DEBUG'))
