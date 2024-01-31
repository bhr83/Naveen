import xmltodict
from collections.abc import MutableMapping
from collections.abc import MutableMapping, Iterable
import sys
import json

file_name = sys.argv[1]

with open(file_name, 'r') as file:
    xml_data = file.read()
xml_dict=xmltodict.parse(xml_data)
#print(xml_dict)

def flatten(dictionary, parent_key='', separator='_'):
    items = []
    for key, value in dictionary.items():
        new_key = parent_key + separator + key if parent_key else key
        items.append((new_key, value))
    return dict(items)
new_dict = flatten(xml_dict)
#print(new_dict)
output = json.dumps(new_dict)
json_output = json.loads(output)
print(json.dumps(new_dict))
