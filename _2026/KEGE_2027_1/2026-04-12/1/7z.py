from ipaddress import *

ipv=ip_network("192.168.108.157/255.255.255.192",0)
n=0
for ip in ipv:
    if str(ip)=='192.168.108.157':
        print (ip,n)
    n+=1