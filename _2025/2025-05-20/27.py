from itertools import *
from fnmatch import *
from functools import *
from math import *
from pickle import *
from sys import *
# setrecursionlimit(100000)


from functools import *
with open("27B.txt") as f:
    s=f.readline()
    a=[[],[],[]]
    for s in f:
        x,y,k=s.replace(',','.').strip().split()

        # print (x,y,k)
        x = float(x)
        y = float(y)
        k = int(k)
        a[k-1].append([x,y])

    cluster=[[],[],[]]
    print (len(a[0]),len(a[1]),len(a[2]),)
    for i in range(len(a)):
        for p1 in a[i]:
            suma=0
            for p2 in a[i]:
                suma=suma+dist(p1,p2)
            cluster[i].append([suma,*p1])
        cluster[i].sort()
    # cluster[1].sort()
    # print (cluster[0][0],cluster[1][0])
    print (cluster[1][:1])
    print(cluster[0][:1])
    print(cluster[2][:1])



