from netmiko import Netmiko

username = 'pyclass'
password = '88newclass'
hostname = 'cisco4.lasthop.io'

device = {
    'host':hostname,
    'username':username,
    'password':password,
    'device_type':'cisco_ios',
   }

conn = Netmiko(**device)

print(conn.find_prompt())
command = 'ping'
output = conn.send_command(command, expect_string='Protocol', strip_prompt=False, strip_command=False)
output += conn.send_command('\n', expect_string='Target IP address', strip_prompt=False, strip_command=False)
output += conn.send_command('8.8.8.8', expect_string='Repeat count', strip_prompt=False, strip_command=False)
output += conn.send_command('\n', expect_string='Datagram size', strip_prompt=False, strip_command=False)
output += conn.send_command('\n', expect_string='Timeout in seconds', strip_prompt=False, strip_command=False)
output += conn.send_command('\n', expect_string='Extended commands', strip_prompt=False, strip_command=False)
output += conn.send_command('\n', expect_string='Sweep range of size', strip_prompt=False, strip_command=False)
output += conn.send_command('\n', expect_string='#', strip_prompt=False, strip_command=False)
conn.disconnect()

print(output)
