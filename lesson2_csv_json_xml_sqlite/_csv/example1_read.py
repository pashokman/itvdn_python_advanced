import csv

file_path = r'C:\Users\PaulKP\Documents\Projects\python\selenium\itvdn_python_advanced\lesson2_csv_json_xml_sqlite\_csv\data\example1.csv'

with open(file_path, 'r') as f:
    reader = csv.reader(f)
    print('Line nums', reader.line_num)
    print('Dialect', reader.dialect)    #dialect - rules to read and write file
    for row in reader:
        print(row)