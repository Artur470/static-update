# app.py

from dotenv import load_dotenv
import os
import psycopg2  # Убедитесь, что у вас установлен этот пакет

# Загружаем переменные окружения из файла .env
load_dotenv()

# Получаем переменные окружения
db_name = os.getenv('DB_NAME')
db_user = os.getenv('DB_USER')
db_password = os.getenv('DB_PASSWORD')
db_host = os.getenv('DB_HOST')
db_port = os.getenv('DB_PORT')

# Переменная для подключения
connection = None

try:
    # Попытка подключения к базе данных
    connection = psycopg2.connect(
        dbname=db_name,
        user=db_user,
        password=db_password,
        host=db_host,
        port=db_port
    )
    print("Соединение с базой данных установлено успешно")
except Exception as e:
    print(f"Ошибка подключения к базе данных: {e}")
finally:
    if connection:
        connection.close()
        print("Соединение с базой данных закрыто")
