from dotenv import load_dotenv
import os

# Загрузите переменные окружения из .env файла
load_dotenv()

# Пример получения переменных
SECRET_KEY = os.getenv('SECRET_KEY')
DEBUG = os.getenv('DEBUG')
EMAIL_HOST_USER = os.getenv('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = os.getenv('EMAIL_HOST_PASSWORD')
CLOUD_NAME = os.getenv('CLOUD_NAME')
API_KEY = os.getenv('API_KEY')
API_SECRET = os.getenv('API_SECRET')
DB_HOST = os.getenv('DB_HOST')
DB_USER = os.getenv('DB_USER')
DB_PASSWORD = os.getenv('DB_PASSWORD')
DB_NAME = os.getenv('DB_NAME')
DB_PORT = os.getenv('DB_PORT')
CLOUDINARY_CLOUD_NAME = os.getenv('CLOUDINARY_CLOUD_NAME')
CLOUDINARY_API_KEY = os.getenv('CLOUDINARY_API_KEY')
CLOUDINARY_API_SECRET = os.getenv('CLOUDINARY_API_SECRET')

print(f"SECRET_KEY: {SECRET_KEY}")
print(f"DEBUG: {DEBUG}")
print(f"EMAIL_HOST_USER: {EMAIL_HOST_USER}")
print(f"EMAIL_HOST_PASSWORD: {EMAIL_HOST_PASSWORD}")
print(f"CLOUD_NAME: {CLOUD_NAME}")
print(f"API_KEY: {API_KEY}")
print(f"API_SECRET: {API_SECRET}")
print(f"DB_HOST: {DB_HOST}")
print(f"DB_USER: {DB_USER}")
print(f"DB_PASSWORD: {DB_PASSWORD}")
print(f"DB_NAME: {DB_NAME}")
print(f"DB_PORT: {DB_PORT}")
print(f"CLOUDINARY_CLOUD_NAME: {CLOUDINARY_CLOUD_NAME}")
print(f"CLOUDINARY_API_KEY: {CLOUDINARY_API_KEY}")
print(f"CLOUDINARY_API_SECRET: {CLOUDINARY_API_SECRET}")
