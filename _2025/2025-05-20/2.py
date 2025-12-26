from itertools import *
from fnmatch import *
from functools import *
from math import *
from pickle import *

def f(x,y,z,w):
    return ( (((not x) or y) and (not w)) and ( z and (not(y and w)))               )

for a1,a2,a3,a4,a5,a6,a7 in product([0,1], repeat=7):
    tab=[(0,a1,a2,1),(a3,1,a4,a5),(1,0,a6,a7)]
    if len(tab)==len(set(tab)):
        for p in permutations('xyzw'):
            if [ f(**dict(zip(p,r))) for r in tab ] == [1,1,1]:
                print (p)

