


print (224&255)

print (31&255)
print (249&240)
print (13&0)
#
#
print (177&128)
print (177&(128+64))
print (177&(128+64+32),128+64+32)
print (177&(128+64+32+16+8))
#
#
#

from ipaddress import *

for mask in range(1,32+1):
    print (ip_network(f"235.116.177.140/{mask}",0))

# 8 8 3
print (int('11100000',2))
# #
# # print(ip_network(f"224.31.249.137/255.255.240.0", 0))
n=0
cnt=0
for ip in ip_network("220.151.212.184/255.255.192.0",0):

    # print (ip,n,bin(int(ip))[2:].zfill(32))
    # print(f"{ip}, {n}, {int(ip):032b}")
    s=bin(int(ip))[2:].zfill(32)
    if s.count('1')%4==0:
        print(f"{ip}, {n}, {int(ip):032b}")

        cnt+=1
    n+=1
print (cnt)

