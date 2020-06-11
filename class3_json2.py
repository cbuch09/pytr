import json

with open('class3_json2.json') as x:
    doc = json.load(x)

arp_info = {}

arp_list = arp_data['ipV4Neighbors']

for arp in arp_list:
    print(arp)
