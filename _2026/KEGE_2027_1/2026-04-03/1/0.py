print(f"{112:b}")
print(bin(172)[2:])
print(120&248)
print(f"{248:b}")
print (112&248)
print (113&248)
print (114&248)
print (115&248)
print (116&248)
print (117&248)
print (118&248)
print (119&248)

from ipaddress import *

ipv="172.16.113.13/255.255.248.0"
mbit=21
ipv=f"64.16.113.13/{mbit}"
cnt=0
print (ip_network(ipv,0))
for ip in ip_network(ipv,0):
    print (ip,cnt,f"{int(ip):032b}")
    # print (bin(int(ip))[2:].zfill(32))
    cnt+=1