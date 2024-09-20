import chardet

def check_file_encoding(file_path):
    with open(file_path, 'rb') as f:
        raw_data = f.read()
    result = chardet.detect(raw_data)
    print(f"Detected encoding: {result['encoding']}")

if __name__ == "__main__":
    check_file_encoding('.env')
