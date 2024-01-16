import csv

sniffer = csv.Sniffer()
dialect = None

file_path = r'C:\Users\PaulKP\Documents\Projects\python\selenium\itvdn_python_advanced\lesson2_csv_json_xml_sqlite\_csv\data\undefined_dialect.csv'

with open(file_path, 'r') as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)

with open(file_path, 'r') as f:
    content = f.read()
    dialect = sniffer.sniff(content)

print(dialect.delimiter, dialect.doublequote, dialect.quoting)

with open(file_path, 'r') as f:
    reader = csv.reader(f, dialect=dialect)
    for row in reader:
        print(row)