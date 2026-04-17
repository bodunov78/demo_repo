print (157&224)
print (bin(200))
print (bin(240))
print (bin(248))

from ipaddress import *

ipv="162.198.0.157/255.255.255.224"
print (ip_network(ipv,0))
cnt=0
for ip in ip_network(ipv,0):
    print
    if str(ip)=="162.198.0.157":
        print (ip,cnt,ip_network(ipv,0).with_netmask)

    cnt+=1

#
# mask=[0,128,128+64,128+64+32,128+64+32+16,128+64+32+16+8,128+64+32+16+8+4,128+64+32+16+8+4+2,128+64+32+16+8+4+2+1]
# print (mask)
#
# for m in mask:
#     print (m,112&m)
#
# for m in range(1,32+1):
#     ipv=f"224.128.112.142/{m}"
#     print (ip_network(ipv,0))
#
