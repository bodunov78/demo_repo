from functools import *
import sys

# sys.setrecursionlimit(10000)
@lru_cache(None)


def fufu(n):
    if n <=0 : return 0
    elif n==1: return 1
    else: return n+fufu(n-1)

# print (fufu(10**6))


for i in range(10**6):
    fufu(i)

print (fufu(10**6))