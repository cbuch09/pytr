from netmiko import Netmiko
from getpass import getpass
import time

password = getpass()
ios4 = {
    'device_type':'cisco_ios',
    'host':'cisco4.lasthop.io',
    'username':'pyclass',
    'password':password,
    'secret':password,
    'session_log':'my_output.txt',
}

conn = Netmiko(**ios4)

conn.enable()
print(conn.find_prompt())
