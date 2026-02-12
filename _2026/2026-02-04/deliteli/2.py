from math import *
from time import *
from itertools import *
from random import *
def fn(n):

    ts=time()
    # n=16
    d=[]
    i=2
    while n>1:
        while n%i==0:
            d.append(i)
            n=n//i
            # print (d)
        i+=1

    # d=set(d)
    deli=[]
    for i in range(1,len(d)):
        m=[prod(x) for x in combinations(d,i)]
        deli.extend(m)

    # print (deli)
    deli=set(deli)
    print (len(deli))
    print (time()-ts)
    return (time()-ts)

# n=(2**5)*(3**3)*(5**5)*(11**5)*(7**4)
# n = randint(110_250_000, 110_300_000)
# for i in range(20):
#     n = randint(110_250_000, 110_300_000)
#     fn(n)

m=[fn(randint(110_250_000, 110_300_000)) for i in range(20)]
print (sum(m)/len(m))
print (m)