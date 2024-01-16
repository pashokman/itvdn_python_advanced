import csv

file_path = r'C:\Users\PaulKP\Documents\Projects\python\selenium\itvdn_python_advanced\lesson2_csv_json_xml_sqlite\_csv\data\output.csv'
quoting = csv.QUOTE_MINIMAL

with open(file_path, 'w') as f:
    # QUOTE_ALL - add quotes all values, QUOTE_MINIMAL - add quotes only if in value there are some spec symbols, 
    # QUOTE_NONE - turn off adding quotes, QUOTE_NONNUMERIC - add quotes only for values that are non numeric.
    writer = csv.DictWriter(
        f,
        fieldnames=['first_name', 'last_name', 'age'],
        quoting=quoting
    ) 
    writer.writeheader()
    writer.writerow({
        'first_name': 'Ivan',
        'last_name': 'Nechui @ ll, Test',
        'age': 20
    })
    writer.writerow({
        'first_name': 'Taras',
        'last_name': 'Shevchenko',
        'age': 30
    })
    writer.writerow({
        'first_name': 'Lesia',
        'last_name': 'Ukrainka',
        'age': 30
    })