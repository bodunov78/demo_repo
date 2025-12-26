from ipaddress import *
cnt=0
for s in ip_network("172.16.168.0/255.255.248.0",0):
    # b=str(bin(s))
    # ip=ip_address(s)
    # print (int(s))
    b=bin(int(s))[2:].zfill(32)
    print(b)
    bn=b.count('1')
    if bn%5!=0:
        cnt+=1

print(cnt)
    # print(bin(int(s))[2:])
    # print (f"{ip:b}")

#
# from ipaddress import *
# net = ip_network('192.168.248.176/255.255.255.240' )
# k = 0
# #получим двоичную запись для каждого значения ip-адреса сети
# for ip in net:
#   b = f'{ip:b}'
# #проверим заданное условие
#   if b.count('1')>b.count('0'):
#     k += 1
# print(k)