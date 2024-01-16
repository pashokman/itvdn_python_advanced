from xml.etree import ElementTree as ET

infile = r'C:\Users\PaulKP\Documents\Projects\python\selenium\itvdn_python_advanced\lesson2_csv_json_xml_sqlite\_xml\data\test.xml'
tree = ET.parse(infile)
root = tree.getroot()
children = list(root)

for studend_data in children:
    print("PK: ", (studend_data.attrib, studend_data.get('pk')))
    print(f"""{studend_data.find('./first_name').text}, {studend_data.find('./last_name').text}, {studend_data.find('./age').text}""")
    
# search value by Xpath
first_names = root.findall('./person/first_name')
last_names = root.findall('./person/last_name')
ages = root.findall('./person/age')

for values in zip(first_names, last_names, ages):
    row = {value.tag: value.text for value in values}
    print(row)

for student_data in children:
    print("PK: ", studend_data.attrib)
    for child in studend_data:
        print(f"{child.tag}: {child.text}")