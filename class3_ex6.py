from netmiko import ConnectHandler
from os import path
import yaml


homedir = path.expanduser('~')
filename = path.join(homedir, '.netmiko.yml')

with open(filename) as x:
    devices = yaml.safe_load(x)

cisco3 = devices['cisco3']

conn = ConnectHandler(**cisco3)

output = conn.find_prompt()

print(output)
