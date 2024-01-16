import datetime
import json

class DateFormatEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, datetime.datetime):
            return {
                'value': obj.strftime('%d.%m.%Y %H:%M:%S'),
                '__datetime__': True
            }
        elif isinstance(obj, datetime.date):
            return {
                'value': obj.strftime('%d.%m.%Y'),
                '__date__': True
            }
        return json.JSONEncoder.default(self, obj)
    

data = {
    'first_name': 'Taras',
    'last_name': 'Shevchenko',
    'birth_date': datetime.date(1815, 7, 15),
    'hired_at': datetime.datetime(1830, 10, 26, 12, 30, 5),
    'hobbies': [
        'cobza',
        'poems',
        'study'
    ]
}

json_data = json.dumps(data, cls=DateFormatEncoder, indent=4)
print(json_data)

file_path_in = r'C:\Users\PaulKP\Documents\Projects\python\selenium\itvdn_python_advanced\lesson2_csv_json_xml_sqlite\_json\data\output.json'
with open(file_path_in, 'w') as f:
    json.dump(data, f, cls=DateFormatEncoder, indent=4)

def as_date_datetime(dct):
    print(dct)
    if '__datetime__' in dct:
        return datetime.datetime.strptime(dct['value'], '%d.%m.%Y %H:%M:%S')
    if '__date__' in dct:
        return datetime.datetime.strptime(dct['value'], '%d.%m.%Y').date()
    return dct

with open(file_path_in, 'r') as f:
    data = json.load(f, object_hook=as_date_datetime)
    print(data)