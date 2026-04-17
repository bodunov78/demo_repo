from random import *
for x in range(1000):
    m=[randint(1,2) for _ in range(5)]
    res=5
    for c in m:
        if c==1:
            res=res*10+1
        else:
            res//=3
    if res==19:
        print (m)

