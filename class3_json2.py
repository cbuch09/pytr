import json
from pprint import pprint

with open('class3_json2.json') as x:
    doc = json.load(x)

arp_info = {}

arp_list = doc['ipV4Neighbors']

for arp in arp_list:
    ip = arp['address']
    mac = arp['hwAddress']
    arp_info[ip] = mac

pprint(arp_info)
