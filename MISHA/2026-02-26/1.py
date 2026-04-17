# s=bin((4**2020)+(2**2017) -15)[2:]
# print (s.count('1'))
# # 56789 - >7 ?
from string import *
def des2n(n,k):
    L=printable
    s=""
    while n>0:
        ost=n%k
        s=L[ost]+s
        n=n//k
    # print (s)
    return s
print (printable)
print(des2n(56782,16))