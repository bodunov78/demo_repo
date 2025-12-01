from itertools import *
from fnmatch import *
from functools import *
from math import *
from pickle import *

def f(x,y,A):
    return ((3*x-2*y<A)or (y>=420) or (x>370))

for A in range(1000,10000):
    m=[f(x,y,A) for x in range(1,1000) for y in range(1,1000)]
    if all(m):
        print(A)
        break

