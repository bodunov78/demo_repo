from sys import *
from math import *
from functools import *
from itertools import *
from turtle import *
from fnmatch import *
from time import *
ts=time()
def dv(n):
    s=""
    while n>0:
        s=str(n%2)+s
        n=n//2
    return s




def r(n):
    s=dv(n)
    s0=s.count('0')
    s1=s.count('1')
    ss=dv(s1)+dv(s0)
    #
    # if n%3==0:
    #     s=s+s[-2:]
    # else:
    #     suma=sum((int(x) for x in s))
    #     s2=dv(suma)
    #     s=s+s2
    return (int(ss,2))

print(r(17))
mini=[]
for i in range(10**10,1,-1):
    ri=r(i)
    if ri==183:
        mini.append(r(i))
        print (i)

mini.sort()
print (mini)
print (time()-ts)