#2231
# Если маска подсети 255.255.255.224 и IP-адрес компьютера в сети 162.198.0.157, то порядковый номер компьютера в сети равен_____
from ipaddress import *
net4 = list(ip_network('162.198.0.157/255.255.255.224',0))
a=0
print (net4)
for x in net4:
    a+=1
    print (f"{bin(int(x))[2:]},{x},{a}")

    #кол-во 1,0
    s=bin(int(x))[2:]
    print (s,s.count('1'),s.count('0'))


# первый в списке адрес сети, последний широковещательный, делаем поправку


#Тип 13 11308
# 203.155.196.98

for i in range(23,24):
    subnet1=ip_network(f"203.155.196.98/{i}", 0)
    # for x in subnet1:
    #     print (x)
    print(subnet1)
