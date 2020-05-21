from netmiko import Netmiko

username = ''
password = ''

nxos1 = {
    'host':'nxos1.lasthop.io',
    'username':username,
    'password':password,
    'device_type':'cisco_nxos',
   }

nxos2 = {
    'host':'nxos2.lasthop.io',
    'username':username,
    'password':password,
    'device_type':'cisco_nxos',
   } 

devices = [nxos1,nxos2]

for dev in devices:
    conn = Netmiko(**dev)
    output = conn.send_config_from_file('config.txt')
    conn.save_config()
    print(output)
    conn.disconnect()

