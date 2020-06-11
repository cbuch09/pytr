import json

with open('json_interfaces.json') as x:
    interfaces = json.load(x)

#print(interfaces)

v4 = []
v6 = []

for interfaces, int_dict in interfaces.items():
    for address, address_dict in int_dict.items():
        for ip, ip_dict in address_dict.items():
            prefix_length = ip_dict['prefix_length']
            if address == 'ipv4':
                v4.append(f'{ip}, {prefix_length}')
            if address == 'ipv6':
                v6.append(f'{ip}, {prefix_length}')

print(f'IPv4 Address: {v4}')
print(f'IPv6 Address: {v6}') 
