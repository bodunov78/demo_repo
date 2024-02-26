from ipaddress import *


#Тип 13 7669


# subnet1 = ip_network('80.0.1.0/28')
for i in range(1,33):
    subnet1=ip_network(f"224.128.112.142/{i}", 0)
    # print(subnet1.with_netmask)
    print(subnet1.with_netmask)

#Тип 13 9363

for i in range(1,33):
    subnet1=ip_network(f"111.81.208.27/{i}", 0)
    print(subnet1.with_netmask)

#Тип 13 11308
# 203.155.196.98

for i in range(1,33):
    subnet1=ip_network(f"203.155.196.98/{i}", 0)
    print(subnet1)
