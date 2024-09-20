# check_db_url.py
import re
from decouple import config

# Создаем строку подключения
db_url = f"postgresql://{config('DB_USER')}:{config('DB_PASSWORD')}@{config('DB_HOST')}:{config('DB_PORT')}/{config('DB_NAME')}"
print("Database URL:", db_url)

# Проверяем на наличие непечатаемых символов
if re.search(r'[^\x00-\x7F]', db_url):
    print("Database URL содержит нестандартные символы")
else:
    print("Database URL не содержит нестандартные символы")
