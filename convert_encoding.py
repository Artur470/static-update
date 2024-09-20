import codecs 
input_file = 'D:\\fdd\\postgreSQLHL\\.env' 
output_file = 'D:\\fdd\\postgreSQLHL\\env_utf8.txt' 
with codecs.open(input_file, 'r', 'utf-8', errors='ignore') as infile: 
    with codecs.open(output_file, 'w', 'utf-8') as outfile: 
        outfile.write(infile.read()) 
