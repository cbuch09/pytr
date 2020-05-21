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
output = conn.send_command_timing(command, strip_prompt=False, strip_command=False)
output += conn.send_command_timing('\n', strip_prompt=False, strip_command=False)
output += conn.send_command_timing('8.8.8.8', strip_prompt=False, strip_command=False)
output += conn.send_command_timing('\n', strip_prompt=False, strip_command=False)
output += conn.send_command_timing('\n', strip_prompt=False, strip_command=False)
output += conn.send_command_timing('\n', strip_prompt=False, strip_command=False)
output += conn.send_command_timing('\n', strip_prompt=False, strip_command=False)
output += conn.send_command_timing('\n', strip_prompt=False, strip_command=False)
conn.disconnect()

print(output)
