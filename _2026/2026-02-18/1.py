from ipaddress import *


mask=22
for mask in range(1,32):
    ipv=ip_network(f"117.14.17.13/{mask}",0)
    cnt=0
    print (ipv,mask)



    # for ip in ipv:
    #     print (ip,cnt)
    #     cnt+=1