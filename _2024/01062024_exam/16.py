from functools import *
from  sys import *
setrecursionlimit(10000)
@lru_cache(None)

def F(n):
    if n == 1:
        return 1
    elif n > 1:
        return n*F(n-1)
# заполняем кэш
for x in range(2024):
    F(x)

print(F(2023)//F(2020))