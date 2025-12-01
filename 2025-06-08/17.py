from sys import *
from math import *
from functools import *
from itertools import *
from turtle import *
from fnmatch import *


def fi(n):
    s=str(abs(n))
    if len(s)==4 and s.count('9')<=1:
        return 1
    else:
        return 0




with open("1002_17.txt") as f :
    m=[]
    for x in f:
        x=x.strip()
        m.append(int(x))

    print (m)

    maxi=max([x for x in m if fi(x)==1])
    print (maxi)
    maxt=-10**20
    cnt=0
    for a1,a2,a3 in zip(m,m[1:],m[2:]):
        if fi(a1)+fi(a2)+fi(a3)<=1 and a1+a2+a3>=maxi:
            maxt=max(maxt,a1+a2+a3)
            cnt+=1
    print (cnt,maxt)


