from itertools import *
from fnmatch import *
from functools import *
from math import *
from pickle import *
from sys import *
# setrecursionlimit(100000)


from functools import *

@lru_cache(None)
def f(n):
    if n>40000 : return n
    if n<=40000 : return ((n+5)*f(n+2))



for i in range(40005,-1,-1):
    f(i)

print ((f(16342)-13*f(16344))/f(16346))




