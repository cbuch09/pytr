from netmiko import ConnectHandler
from os import path
from ciscoconfparse import CiscoConfParse
import yaml



homedir = path.expanduser('~')
filename = path.join(homedir, '.netmiko.yml')

with open(filename) as x:
    devices = yaml.safe_load(x)

cisco4 = devices['cisco4']

conn = ConnectHandler(**cisco4)

output = conn.send_command('show run')

config = CiscoConfParse(output.splitlines())

interfaces = config.find_objects_w_child(parentspec=r'^interface',childspec=r'^\s+ip address')

for interface in interfaces:
    print(f'Interface: {interface.text}')
    ip = interface.re_search_children(r'ip address')[0].text
    print(f'IP = {ip}')
