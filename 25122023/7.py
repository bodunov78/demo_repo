from functools import *
import sys
sys.setrecursionlimit(10000)
@lru_cache(None)


def fufu(n):
    global d
    if n<3 :
        d.append(1)
        return 1

    elif n>2 and n%2==1:
        k=fufu(n-1)+fufu(n-2)
        d.append(k)
        return k
    elif n>2 and n%2==0:
        return sum(fufu(i) for i in range(1,n))

d=[]
for i in range(1,24+1):
    print (fufu(i))
