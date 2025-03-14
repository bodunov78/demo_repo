from ipaddress import *
ipa="172.16.18.19"
ips=f"{IPv4Address(ipa):b}"[20:]
print (ips)
for x in range(256):
    ips=ip_network(f"183.{x}.177.0/255.255.252.0",0)
    print (ips)

ipss = ip_network(f"183.199.177.0/255.255.252.0", 0)
for x in ipss:
    print (x)
#
#
#
#
# for A in range(256):
#     ips=ip_network(f"183.192.{A}.0/255.255.252.0",0)
#     flag=1
#     for x in ips:
#         ipb=f"{IPv4Address(x):b}"[16:]
#         if ipb.count('1')<=3:
#             flag=0
#             break
#     if flag==1:
#         print (ips,A)
#
#
#
# #
# # #Тип 13 2231
# #
# #
# # # 162.198.0.157
# # # 255.255.255.224
# # net4 = list(ip_network('162.198.0.157/255.255.255.224',0))
# # #net4 = ip_network('162.198.0.157/255.255.255.224',0)
# #
# #
# #
# # print (len(net4))
# # num=0
# # for x in net4:
# #     num+=1
# #     print (x,num)
# #     if '162.198.0.157' in str(x):
# #         print (x,num)
# # #print (net4)
# #
#
# # #Тип 13 7669
# #
# #
# # # subnet1 = ip_network('80.0.1.0/28')
# # for i in range(1,33):
# #     subnet1=ip_network(f"224.128.112.142/{i}", 0)
# #     print(subnet1.with_netmask)
# #
# # #Тип 13 9363
# #
# # for i in range(1,33):
# #     subnet1=ip_network(f"111.81.208.27/{i}", 0)
# #     print(subnet1.with_netmask)
# #
# # #Тип 13 11308
# # # 203.155.196.98
# #
# # for i in range(1,33):
# #     subnet1=ip_network(f"203.155.196.98/{i}", 0)
# #     print(subnet1)
#
# #Тип 13 60255
# # Сеть задана IP-адресом 192.168.32.160 и маской сети 255.255.255.240.
# # Сколько в этой сети IP-адресов, для которых сумма единиц в двоичной записи IP-адреса чётна?
# # В ответе укажите только число.
#
# subnet=ip_network("192.168.32.160/255.255.255.240",0)
# for x in subnet:
#     ipb=bin(int(IPv4Address(x)))[2:]
#     ipb=f"{IPv4Address(x):n}"
#     print (IPv4Address(x),IPv4Address(x)-200)
#     print (ipb,ipb.count('1'),subnet)
#
# # for addr in IPv4Network('192.168.32.0/28'):
# #     print(f"{IPv4Address(addr):b}")