from xml.etree import ElementTree as ET

infile = r'C:\Users\PaulKP\Documents\Projects\python\selenium\itvdn_python_advanced\lesson2_csv_json_xml_sqlite\_xml\data\test.xml'
tree = ET.parse(infile)
root = tree.getroot()

# search value by Xpath
first_names = root.findall('./person[@pk="21"]/first_name')
last_names = root.findall('./person[@pk="21"]/last_name')
ages = root.findall('./person[@pk="21"]/age')

for values in zip(first_names, last_names, ages):
    row = {value.tag: value.text for value in values}
    print(row)

# return 1 element or None
first_name = root.find('./person/age/..[@pk][1]/first_name')[0].text
print(first_name)

# return list of elements or empty list
first_name = root.findall('./person/age/..[@pk][2]/first_name')[0].text
print(first_name)

first_name = root.findall('./person/age/..[@pk][3]/first_name')[0].text
print(first_name)