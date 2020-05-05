from netmiko import Netmiko

nxos1 = {
    'device_type':'cisco_nxos',
    'host':'nxos1.lasthop.io',
    'username':'',
    'password':'',
}

nxos2 = {
    'device_type':'cisco_nxos',
    'host':'nxos2.lasthop.io',
    'username':'',
    'password':'',
}

devices = [nxos1, nxos2]

for dev in devices:
    conn = Netmiko(**dev)
    conn.enable()
    ver = conn.send_command('show ver')
    print(ver)
