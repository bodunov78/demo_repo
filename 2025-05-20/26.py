from itertools import *
from fnmatch import *
from functools import *
from math import *
from pickle import *
from sys import *
# setrecursionlimit(100000)


from functools import *
with open("1001_26.txt") as f:
    n=f.readline()
    # print (n)
    m=[]
    for x in f:
        a=tuple(map(int,x.split()))
        m.append(a)
    print (len(m))
    m=list(set(m))
    m.sort()
    cnt=1
    k=[]
    for i in range(1,len(m)):
        if m[i-1][0]==m[i][0] and m[i][1]-m[i-1][1]==1:
            cnt+=1
            k.append([cnt,m[i][0]])
        else:
            cnt=1
    k.sort(reverse=1)
    print (k[0])
    for x in k:
        if x[0]==145:
            print (x)