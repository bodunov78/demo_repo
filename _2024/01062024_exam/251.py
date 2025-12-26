from itertools import *
from math import *
from time import *
from functools import *
from  sys import *
setrecursionlimit(10000)

def delit(m):
    # m=[1,2,2,2,2]
    di=set()
    for x in range(1,len(m)+1):
        for y in permutations(m,x):
            # print(y,prod(y))
            di.add(prod(y))
    # print (di)
    return(di)
@lru_cache(None)
def simpl(x):
    di={2,3}
    for k in range(5,x+1,2):
        a=any([k%i==0 for i in di ])
        if not(a):
            di.add(k)

    return di
print (simpl(2**7*3**5))


def get_deli(x):
    deli=[1]
    si=simpl(x)
    # print (si)
    while x>1:
        for d in si:
            # print ("d",d,deli,x)
            while x%d==0:
                  deli.append(d)
                  x//=d
    #print(deli)
    return(deli)

# m=get_deli(1002)
# print(m)
# print (delit(m))

ts=time()
x=2**5*3**4
a=[]
for i in range(1,x+1):
    if x%i==0:
        a.append(i)
print (a,time()-ts)

ts=time()
m=get_deli(x)
print (m)
print (delit(m),time()-ts)
