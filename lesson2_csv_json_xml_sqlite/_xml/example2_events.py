# pip intrall lxml
from lxml import etree as ET


class PersonTarget :

    def __init__(self):
        self.records = []
        self.current_index = None
        self.current_node = None

    def start(self, tag, attrib):
        if tag == 'person':
            self.records.append({
                'first_name': '',
                'last_name': '',
                'age': None,
            })
            self.current_index = len(self.records) - 1
        self.current_node = tag

    def end(self, tag):
        self.current_node = ''

    def data(self, data):
        # print(f"Data: {self.current_node} -> {data}")
        if self.current_node in ['first_name', 'last_name', 'age']:
            self.records[self.current_index][self.current_node] = data

    def close(self):
        return self.records
    
parser = ET.XMLParser(target=PersonTarget())
infile = r'C:\Users\PaulKP\Documents\Projects\python\selenium\itvdn_python_advanced\lesson2_csv_json_xml_sqlite\_xml\data\test.xml'

results = ET.parse(infile, parser)

for r in results:
    print(r)