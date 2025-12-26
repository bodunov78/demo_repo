from itertools import *


def f(x, y, z, w):
    # ((y → z) ∨ (¬x ∧ w)) ≡ (w ≡ z)
    return (((y<=z) or (not(x) and w)) == (w==z))

#18550
def vah():
    for a1, a2, a3 in product([0, 1], repeat=3):
        tab = [(a1, 1, 0, 0), (0, 0, 0, 1), (0, 1, a2, a3)]
        if len(tab) == len(set(tab)):
            for p in permutations('xyzw'):
                if [f(**dict(zip(p, r))) for r in tab] == [1, 1, 1]:
                    print(p)

def nevax():
    print('w', 'y', 'z', 'x')
    for x in (0,1):
        for y in (0,1):
            for z in (0,1):
                for w in (0,1):
                    if f(w,y,z,x) ==1:
                        print (w,y,z,x,f(w,y,z,x))
def nevax2():
    print ('x','y','z','w')
    for a in product((0,1),repeat=4):
        if f(a[0], a[1], a[2], a[3]) == 1:
            print(a[0], a[1], a[2], a[3], f(a[0], a[1], a[2], a[3]))


# vah()
nevax2()


##from itertools import *
##def f(x,y,w,z):
##    return ((not y)<=(z==w))and ((z<=x)==w)

##for a1,a2,a3 in product ([0,1], repeat=3 ):
##    tab=[(1,1,0,1),(0,1,1,a3),(0,a1,a2,0)]
##    print(tab,len(tab),len(set(tab)))
####    
####    if len(tab)==len(set(tab)):
##    for p in permutations('xyzw'):
##        if [f(**dict(zip(p,r))) for r in tab] == [1,1,1]:
##            print (p)

##
##from itertools import *
##
##def f(x,y,z,w):
##    return(((x<=y)==(w<=x)) and (z<=w))
##
##
##for a1,a2,a3,a4 in product ([0,1], repeat=4):
##    tab=[(1,0,0,1),(1,a1,a2,0),(a3,0,1,a4)]
##    if len(tab)==len(set(tab)):
##        for p in permutations('xyzw'):
##            if [f(**dict(zip(p,r)))  for r in tab]==[1,1,1]:
##                print (p)
