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

ios1 = {
    'device_type':'cisco_ios',
    'host':'cisco3.lasthop.io',
    'username':'pyclass',
    'password':'88newclass',
}

devices = [nxos1, nxos2]

for dev in devices:
    conn = Netmiko(**dev)
    conn.enable()
    cmd = conn.find_prompt()
    print(cmd)

ios_conn = Netmiko(**ios1)
ios_conn.enable()
cmd_ios = ios_conn.send_command('show ver')
print(cmd_ios, file=open('ios1_ver.txt','w'))

