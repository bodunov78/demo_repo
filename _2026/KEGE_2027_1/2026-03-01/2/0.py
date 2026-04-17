# # 192.168.37.19
# # 255.255.255.0
# print (192&255)
# print (168&255)
# print (47&240)
# print (255&0)
#
# #
from string import *
from ipaddress import *

cnt=0
ipv=ip_network("192.168.19.13/255.255.255.240",0)
for ip in ipv:
    print (ip,cnt)
    cnt+=1
# print (ipv)

s="asdfghjkl"
# for i in range(len(s)):
#     print (i,s[i])
# for c in s:
#     print (c)
a=[1,2,3,4,77,79]
for i,v in enumerate(a):
    a[i]=v**2
#
# 88x4y_9+7x44y_11.
#
# a=y*9**0+4*9**1+x*9**2+8*9**3+8*9**4+8*9**5
# 88040_9 +y+x*9**2
# L="0123456789abcdefghikl"

print (printable)
for x in range(9):
    for y in range(9):
        a= int(f"88{printable[x]}4{printable[y]}", 9) + int(f"7{printable[x]}44{printable[y]}", 11)
        print (a)