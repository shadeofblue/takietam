import ipaddress

net = ipaddress.ip_network("192.168.0.0/255.255.255.252")

print("addr", net.network_address)
print("hostmask", net.hostmask)
print("netmask", net.netmask)
print("with_netmask", net.with_netmask)
print("with_hostmask", net.network_address)
print("num addresses", net.num_addresses)
print("exploded", net.exploded)
print("with_prefixlen", net.with_prefixlen)
print("compressed", net.compressed)
