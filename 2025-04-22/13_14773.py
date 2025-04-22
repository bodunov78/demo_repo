# 14:00
from ipaddress import *


for x in range(1,33):
    s=ip_network(f"93.138.161.94/{x}",0)
    print (x,s)

# 14:04