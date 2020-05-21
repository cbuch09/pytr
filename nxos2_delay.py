from netmiko import Netmiko
from datetime import datetime

username = 'pyclass'
password = '88newclass'
hostname = 'nxos2.lasthop.io'

device = {
    'host':hostname,
    'username':username,
    'password':password,
    'device_type':'cisco_nxos',
    'global_delay_factor':2,
   }

conn = Netmiko(**device)

print(conn.find_prompt())
print(datetime.now())
command = 'show lldp neighbors detail'
output = conn.send_command(command, delay_factor=8)
#output = conn.send_command(command)
print(output)
print(datetime.now())
conn.disconnect()
