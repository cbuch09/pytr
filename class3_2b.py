import yaml
from pprint import pprint

devices = []

with open('class3_2b.yml','w') as x:
  yaml.dump(devices, x, default_flow_style=False)
  
print(x)
pprint(devices)
