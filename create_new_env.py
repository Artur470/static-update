# create_new_env.py
import io

original_file = '.env'
new_file = '.env_utf8'

try:
    with io.open(original_file, 'r', encoding='utf-8', errors='ignore') as f:
        content = f.read()

    with io.open(new_file, 'w', encoding='utf-8') as f:
        f.write(content)

    print(f"New file created with UTF-8 encoding: {new_file}")

except Exception as e:
    print(f"An error occurred: {e}")
