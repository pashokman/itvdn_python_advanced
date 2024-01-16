import json

data = {
    'first_name': 'Taras',
    'last_name': 'Shevchenko',
    'age': 40,
    'hobbies': [
        'cobza',
        'poems',
        'study'
    ]
}

# dump string from json
json_data = json.dumps(data)
print(json_data)

file_path_out = r'C:\Users\PaulKP\Documents\Projects\python\selenium\itvdn_python_advanced\lesson2_csv_json_xml_sqlite\_json\data\output.json'

with open(file_path_out, 'w') as f:
    # dump json data into a file
    json.dump(data, f, indent=4) # indent - add formatting - add 4 spaces