from itertools import *
from fnmatch import *
from functools import *
from math import *
from pickle import *
from sys import *
# setrecursionlimit(100000)


from functools import *


def tri(a):
    if len(str(abs(a)))==4 and str(abs(a)).count('3')==2:
        return 1
    else:
        return 0




with open("1004_17.txt") as f:
    m= [ int(x) for x in f]
    maxd=[x for x in m if tri(x)]
    print (max(maxd))
    maxi=max(maxd)
    print (len(m))
    cnt=0
    sums=[]
    for a1,a2,a3 in zip(m,m[1:],m[2:]):
        suma=a1+a2+a3
        if tri(a1)+tri(a2)+tri(a3)<=2 and suma<= maxi:
            sums.append(suma)
            cnt+=1

    print (cnt,max(sums))