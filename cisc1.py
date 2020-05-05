from netmiko import Netmiko

host = 'nxos1.lasthop.io'
username = 'pyclass'
password = '88newclass'

nxos1 = {
    'device_type':'cisco_nxos',
    'host':'nxos1.lasthop.io',
    'username':'pyclass',
    'password':'88newclass',
}

nxos2 = {
    'device_type':'cisco_nxos',
    'host':'nxos2.lasthop.io',
    'username':'pyclass',
    'password':'88newclass',
}

devices = [nxos1, nxos2]

for dev in devices:
    conn = Netmiko(**dev)
    conn.enable()
    ver = conn.send_command('show ver')
    print(ver)
