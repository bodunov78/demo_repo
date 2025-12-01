from itertools import *
from fnmatch import *
from functools import *
from math import *
from pickle import *
from sys import *
# setrecursionlimit(100000)


from functools import *
for i in range(0,10**10+1,52412):
    s=str(i)
    pat="91*2?6?4"
    if fnmatch(s,pat):
        print (i,i//52412)
