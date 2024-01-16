import csv

file_path = r'C:\Users\PaulKP\Documents\Projects\python\selenium\itvdn_python_advanced\lesson2_csv_json_xml_sqlite\_csv\data\output.csv'

with open(file_path, 'w') as f:
    # QUOTE_ALL - add quotes all values, QUOTE_MINIMAL - add quotes only if in value there are some spec symbols, 
    # QUOTE_NONE - turn off adding quotes, QUOTE_NONNUMERIC - add quotes only for values that are non numeric.
    writer = csv.writer(f, quoting=csv.QUOTE_MINIMAL) 
    writer.writerow(['1', '2', '3'])
    writer.writerow(['1', '2', '3'])
    writer.writerow(['1', '2', '3'])
    writer.writerow(['1', '2', '3'])
    writer.writerow(['1', '2', '3'])