# test_db_connection.py
import psycopg2
from decouple import config

def test_connection():
    try:
        conn = psycopg2.connect(
            dbname=config('DB_NAME'),
            user=config('DB_USER'),
            password=config('DB_PASSWORD'),
            host=config('DB_HOST'),
            port=config('DB_PORT'),
            options="-c client_encoding=UTF8"  # Явное указание кодировки
        )
        print("Connection successful")
        conn.close()
    except Exception as e:
        print("Error:", e)

if __name__ == "__main__":
    test_connection()
