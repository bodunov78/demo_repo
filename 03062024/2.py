from itertools import *
#from functools import*
#from adx import *


def f0(x,y,z,w):
    return ((y<=z)and (not (w==z) and x))

def f11(x,y,z,w):
    return ((x or not(y)) <= (w == z))

def f12(x,y,z,w):
    return ((x or not(y) )==(w<=z) )

def f_1():
    for a1,a2,a3,a4 in product([0,1],repeat=4):
        tab=[(0,a1,0,1),(a2,0,a3,a4),(1,0,0,1)]
        if len(tab)==len(set(tab)):
            for p in permutations('xyzw'):
                if [f(**dict(zip(p,r))) for r in tab] :
                    print(p)



def f_2():
    for a1,a2,a3,a4,a5,a6 in product([0,1],repeat=6):
        tab=[(0,a1,0,0),(a2,1,1,a3),(a4,0,0,0)]
        if len(tab)==len(set(tab)):
            for p in permutations('xyzw'):
                if [f11(**dict(zip(p,r))) for r in tab] == [0,0,a5]  and [f12(**dict(zip(p,r))) for r in tab] == [0,a6,0]:
                    print(p)


f_2()