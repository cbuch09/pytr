from netmiko import Netmiko

username = ''
password = ''
hostname = 'cisco4.lasthop.io'

device = {
    'host':hostname,
    'username':username,
    'password':password,
    'device_type':'cisco_ios',
   }

conn = Netmiko(**device)

print(conn.find_prompt())

ver = conn.send_command('show ver', use_textfsm=True)
lldp = conn.send_command('show lldp neigh', use_textfsm=True)

print(ver)
print(lldp[0]['neighbor_interface'])

conn.disconnect()
