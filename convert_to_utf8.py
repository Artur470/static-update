import codecs

input_file = '.env'
output_file = '.env_utf8'

with codecs.open(input_file, 'r', 'cp1251', errors='ignore') as infile:
    with codecs.open(output_file, 'w', 'utf-8') as outfile:
        outfile.write(infile.read())
