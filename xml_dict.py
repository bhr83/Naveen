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

        if isinstance(value, MutableMapping):
            items.extend(flatten(value, new_key, separator=separator).items())
        elif isinstance(value, Iterable) and not isinstance(value, str):
            # If the value is a list, flatten each item with index prefix
            for i, item in enumerate(value):
                items.extend(flatten({f"{new_key}_{i}-{k}": v for k, v in item.items()}, separator=separator).items())
        else:
            items.append((new_key, value))
    return dict(items)
new_dict = flatten(xml_dict)
#print(new_dict)
output = json.dumps(new_dict)
json_output = json.loads(output)
print(json.dumps(new_dict))
