from itertools import *
def f1(x,y,z,w):
    return ((x<=y) == (w or (not(z))))

def f2(x,y,z,w):
    return ( (x<=y) and ((not(w))==z))


for a1,a2,a3,a4,a5 in product([0,1],repeat=5):
    tab=[(a1,1,0,1),(a2,0,0,0),(0,a3,0,0)]
    if len(tab)==len(set(tab)):
        for p in permutations('xyzw'):
            if [f1(**dict(zip(p,r))) for r in tab] == [a4,0,0] and [f2(**dict(zip(p,r))) for r in tab] == [0,a5,1]:
                print (p)
