from sys import *
from math import *
from functools import *
from itertools import *
from turtle import *
from fnmatch import *

with open("1003_26.txt") as f :
    s=f.readline()
    a=[]
    for s in f:
        m=tuple(map(int,s.split()))
        a.append(m)
        a=list(set(a))
    # m=[[int(x),int(y)] for x,y in f]
    #     print (m)

    a.sort()
    print (a[:10])
    cnt=1
    k=[]
    for i in range(1,len(a)):
        if a[i-1][0]==a[i][0] and a[i][1]-a[i-1][1]==1:
            cnt+=1
            k.append([cnt,a[i]])
        else:
            cnt=1
    print (max(k))
    for x in k:
        if x[0]==150:
            print (x)
