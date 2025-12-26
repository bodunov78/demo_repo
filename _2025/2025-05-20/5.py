from itertools import *
from fnmatch import *
from functools import *
from math import *
from pickle import *
def tri(n):
    s=""
    while n:
        s=str(n%3)+s
        n=n//3

    return s

def che(s):
    if s[-1]=='0':
        s+=s[-2:]
    else:
        m=sum(int(x) for x in s)
        m=tri(m)
        s=s+m
    return s
a=[]
for n in range(1,100):
    r=int(che(tri(n)),3)
    if r >123:
        print (n,r)
        a.append(r)
a.sort()
print (int(che(tri(129)),3))
print (141)
