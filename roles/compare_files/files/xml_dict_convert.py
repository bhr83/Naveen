import sys
import xmltodict
import json
from collections.abc import MutableMapping

file_name = sys.argv[1]

with open(file_name, 'r') as file:
    xml_data = file.read()
xml_dict=xmltodict.parse(xml_data)

def flatten(dictionary, parent_key='', separator='_'):
    items = []
    for key, value in dictionary.items():
        new_key = parent_key + separator + key if parent_key else key
        if isinstance(value, MutableMapping):
            items.extend(flatten(value, new_key, separator=separator).items())
        else:
            items.append((new_key, value))
    return dict(items)


new_dict = flatten(xml_dict)
#print(new_dict)
output = json.dumps(new_dict)
json_output = json.loads(output)
print(json.dumps(new_dict))
