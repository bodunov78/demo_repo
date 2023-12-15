from random import *

d=dict()
rnd=[randint(1,100) for x in range(100)]
print(rnd)
for j in set(rnd):
    d[j]=rnd.count(j)

print(set(rnd))
print(d)

