# print_env_vars.py
from decouple import config

print("DB_NAME:", config('DB_NAME'))
print("DB_USER:", config('DB_USER'))
print("DB_PASSWORD:", config('DB_PASSWORD'))
print("DB_HOST:", config('DB_HOST'))
print("DB_PORT:", config('DB_PORT'))
