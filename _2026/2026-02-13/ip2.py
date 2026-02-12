from ipaddress import *



s=f"192.168.20.0/255.255.254.0"
n=0
for i in ip_network(s,0):
    print (i,n)
    n+=1