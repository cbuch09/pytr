from ciscoconfparse import CiscoConfParse

bgp_output = '''
router bgp 44
 bgp router-id 10.220.88.38
 address-family ipv4 unicast
 !
 neighbor 10.220.88.20
  remote-as 42
  description pynet-rtr1
  address-family ipv4 unicast
   route-policy ALLOW in
   route-policy ALLOW out
  !
 !
 neighbor 10.220.88.32
  remote-as 43
  address-family ipv4 unicast
   route-policy ALLOW in
   route-policy ALLOW out
'''

bgp_parse = CiscoConfParse(bgp_output.splitlines())

neigh = bgp_parse.find_objects_w_parents(parentspec=r'router bgp',childspec=r'neighbor')

peers = []

for n in neigh:
    _, neighbor_ip = n.text.split()
    for child in n.children:
        if 'remote-as' in child.text:
            _, asn = child.text.split()
    peers.append((neighbor_ip, asn))

print(f'Peers: {peers}')
