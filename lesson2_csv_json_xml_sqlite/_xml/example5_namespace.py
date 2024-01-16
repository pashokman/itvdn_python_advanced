from lxml import etree as ET

XML_NS = {'xsi': 'http://www.w3.org/2001/XMLSchema-instance'}

infile = r'C:\Users\PaulKP\Documents\Projects\python\selenium\itvdn_python_advanced\lesson2_csv_json_xml_sqlite\_xml\data\test_ns.xml'
root = ET.parse(infile)

# first case of geting values with ns
for person in root.findall('{http://example.com/persons}person'):   #default namespace
    name = person.find('{http://example.com/persons}name').text     #default namespace
    alias = person.find('{http://example.com/olympic}name').text    #olympic namespace
    field = person.find('{http://example.com/olympic}field').text   #olympic namespace
    print(f"{name}, {field}, -> {alias}")

print('\n')

# second case of geting values with ns
ns = {
    'persons': 'http://example.com/persons',
    'olympic': 'http://example.com/olympic'
}

for person in root.findall('persons:person', ns):   #default namespace
    name = person.find('persons:name', ns).text     #default namespace
    alias = person.find('olympic:name', ns).text    #olympic namespace
    field = person.find('olympic:field', ns).text   #olympic namespace
    print(f"{name}, {field}, -> {alias}")