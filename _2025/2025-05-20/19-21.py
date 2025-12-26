from itertools import *
from fnmatch import *
from functools import *
from math import *
from pickle import *
from sys import *
# setrecursionlimit(100000)


from functools import *

def f(s,m):
    if s>=89: return m%2==0
    if m==0 : return 0
    h=[f(s+2,m-1),f(s+4,m-1),f(s*5,m-1)]
    return any(h) if (m-1)%2==0 else  all(h)

print ("19",[s for s in range(1,88+1) if  f(s,2)])
print ("20",[s for s in range(1,88+1) if not f(s,1) and  f(s,3)])
print ("21",[s for s in range(1,88+1) if not f(s,2) and f(s,4)])
