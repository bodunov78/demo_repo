from ipaddress import *



s=f"1.168.20.0/255.255.254.0"
n=0
print (ip_network(s,0))
for i in ip_network(s,0):
    print (i,n,bin(int(i))[2:].zfill(32))
    print(i, n, f"{int(i):032b}" )

    n+=1
