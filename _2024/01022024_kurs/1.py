from random import *
i=set()

m=[set() for i in range(10)]
m[0].add(1)
print (m)


m=[[randint(0,100) for j in range(10 )] for i in range(10)]
print (m)

mt=[[m[i][j] for i in range(len(m))] for j in range(len(m))]
ms=sum(m,[])
print (set(ms))

s="12 24 -25 26.0 -44 22 22 44"



m=list(s.split())
for x in m:
    if isinstance(x,float):
        print (x)

print (m)