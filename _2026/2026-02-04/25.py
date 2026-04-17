from time import *
from itertools import *
from math import *
ts=time()

def deli(n):
    i=2
    a=[]
    while n > 1:
        while n % i == 0:
            a.append(i)
            n = n // i
        if i>2:
            i += 2
        else:
            i+=1
    # print(a)


    m = []
    for i in range(1, len(a)):
        if i%1000==0:
            print(i)
        d = {prod(x) for x in combinations(a, i)}
        m.extend(d)

    m.sort(reverse=1)
    if len(m)>=2:

        return(sum(m[:2]))
    else:
        return 0

for n in range(110_250_000,110_300_000+1):
    d=deli(n)
    if d%10000==1002:
        print (n,d)
print (time()-ts)