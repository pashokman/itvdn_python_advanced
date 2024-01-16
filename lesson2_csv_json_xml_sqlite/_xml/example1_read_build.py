from xml.etree import ElementTree as ET

file_path_in = r'C:\Users\PaulKP\Documents\Projects\python\selenium\itvdn_python_advanced\lesson2_csv_json_xml_sqlite\_xml\data\test.xml'
file_path_out = r'C:\Users\PaulKP\Documents\Projects\python\selenium\itvdn_python_advanced\lesson2_csv_json_xml_sqlite\_xml\data\output.xml'

tree = ET.parse(file_path_in)
root = tree.getroot()

children = list(root)

for student_data in children:
    print("PK: ", student_data.attrib)
    for child in student_data:
        print(f"{child.tag} {child.text}")


# create new xml file output
root = ET.Element('record')
for i in range(10):
    sub_element = ET.SubElement(root, f"value{i}")
    sub_element.text = str(i * 10)

print(ET.dump(root)) # only for dev/trace

data = [
    {'x': 10, 'y': 29, 'z': 90},
    {'x': 11, 'y': 28, 'z': 91},
    {'x': 12, 'y': 27, 'z': 92},
    {'x': 13, 'y': 26, 'z': 93},
    {'x': 14, 'y': 25, 'z': 94},
]

root = ET.Element('records')

for item in data:
    record = ET.SubElement(root, 'record')
    for key, value in item.items():
        e = ET.SubElement(record, key)
        e.text = str(value)

tree = ET.ElementTree(root)
tree.write(file_path_out, encoding='utf-8')