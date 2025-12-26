#1:19
from functools import *
# from sys import *



@lru_cache(None)
def f(n):
    if n<5 : return n
    if n>=5 : return 2*n*f(n-4)




for i in range(13770):
    f(i)

print ((f(13766)-9*f(13762))/f(13758))

#1:22