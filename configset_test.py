from netmiko import Netmiko
from datetime import datetime

username = 'pyclass'
password = '88newclass'
hostname = 'cisco4.lasthop.io'

device = {
    'host':hostname,
    'username':username,
    'password':password,
    'device_type':'cisco_ios',
    'fast_cli':True
   }

conn = Netmiko(**device)

print(conn.find_prompt())

cmd_set = ['ip name-server 1.1.1.1', 'ip name-server 1.0.0.1', 'ip domain-lookup']

print(datetime.now())

output = conn.send_config_set(cmd_set)
print(output)

print(datetime.now())

conn.disconnect()

