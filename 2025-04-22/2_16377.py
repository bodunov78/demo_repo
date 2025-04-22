#13:31
from itertools import *

def f(x,y,z,w):
    return (((x<=y)==(y<=z)) and(y or w))


for a1,a2,a3,a4,a5,a6 in product([0,1],repeat=6):
    tab=[(0,a1,0,a2),(0,0,a3,0),(a4,a5,a6,0)]
    if len(tab)==len(set(tab)):
        for p in permutations("xyzw"):
            if [f(**dict(zip(p,r))) for r in tab] ==[1,1,1]:
                print (p)

 #13:35