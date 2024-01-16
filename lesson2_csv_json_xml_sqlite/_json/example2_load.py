import datetime
import json

json_data = '{"first_name": "Taras"}'
# load json from string
data = json.loads(json_data) 
print(data)

file_path_in = r'C:\Users\PaulKP\Documents\Projects\python\selenium\itvdn_python_advanced\lesson2_csv_json_xml_sqlite\_json\data\output.json'

with open(file_path_in, 'r') as f:
    # load json from file
    data = json.load(f)
    print(data)

# does not work because method dumps can not work with datetime format 
# data = {
#     'current_date': datetime.datetime.now()
# }

# json_data = json.dumps(data)
# print(json_data)