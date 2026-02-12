from ipaddress import *



s=f"220.151.212.184/255.255.192.0"
n=0
for i in ip_network(s,0):

    s=bin(int(i))[2:].zfill(32)
    cnt=s.count('1')
    if cnt%4==0:
        print(i, n, bin(int(i))[2:].zfill(32),cnt)

    n+=1