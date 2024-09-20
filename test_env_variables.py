import os

# Установите переменные окружения вручную
os.environ['SECRET_KEY'] = 'django-insecure-mo6l7ga_yb$&hzdi%6iye)w%$f8&#fj_18yaesyknd0h^*9hdb'
os.environ['DEBUG'] = 'True'

# Выведите их, чтобы убедиться
print("SECRET_KEY:", os.getenv('SECRET_KEY'))
print("DEBUG:", os.getenv('DEBUG'))
