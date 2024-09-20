import chardet

with open('.env', 'rb') as file:
    result = chardet.detect(file.read())
    print(result)
