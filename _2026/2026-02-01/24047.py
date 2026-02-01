from ipaddress import *

net=ip_network("23.78.143.87/255.255.240.0",0)
cnt=0
for x in net:
    m=str(x)


    m=[bin(int(x))[2:] for x in m.split('.')]

    while '0' in m:
        m.remove('0')

    a = len("".join(m))

    if a<26:
        cnt+=1
        print (m,a)
print (cnt)