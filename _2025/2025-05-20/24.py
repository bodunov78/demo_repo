from itertools import *
from fnmatch import *
from functools import *
from math import *
from pickle import *
from sys import *
# setrecursionlimit(100000)


from functools import *

with open("1002_24.txt") as f:
    s=f.readline().strip()
    print (len(s))

    m=3*95
    a=[]
    for l in range(len(s)):
        for r in range(l+m,len(s)):
            ss=s[l:r+1]
            if ss.count('WQR')==95 and ss[-3:]=='WQR':
                m=max(m,len(ss))
            elif ss.count('WQR')>95:
                break
    print(m)