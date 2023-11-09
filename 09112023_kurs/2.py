from random import *

d=dict()

rnd=[randint(1,10) for x in range(1000)]
#
print (rnd)

for j in set(rnd):
    d[j]=rnd.count(j)

print(set(rnd))
print(sorted(d.values()))

