import os
import psycopg2
from dotenv import load_dotenv

# Загрузите переменные окружения из .env файла
load_dotenv()

# Получите параметры подключения из переменных окружения
DB_HOST = os.getenv('DB_HOST')
DB_USER = os.getenv('DB_USER')
DB_PASSWORD = os.getenv('DB_PASSWORD')
DB_NAME = os.getenv('DB_NAME')
DB_PORT = os.getenv('DB_PORT')

# Попробуйте подключиться к базе данных
try:
    connection = psycopg2.connect(
        host=DB_HOST,
        user=DB_USER,
        password=DB_PASSWORD,
        dbname=DB_NAME,
        port=DB_PORT,
        options="-c client_encoding=UTF8"  # Установка кодировки клиента
    )
    print("Подключение к базе данных успешно!")
    # Не забудьте закрыть соединение после проверки
    connection.close()
except Exception as e:
    print(f"Ошибка при подключении к базе данных: {e}")
