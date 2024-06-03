from random import *

d=dict()
rnd=[randint(1,100) for x in range(100)]
print(rnd)
for j in rnd:
    d[j]=d.get(j,0)+1

print(set(rnd))
print(max(d),max(d.values()),d)

