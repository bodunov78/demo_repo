from itertools import *
a=[32,3,37,8,2,17,1]
b=[i for i in range(1,101)]
for i in range(1,8):
    for c in permutations(a,i):
        s=sum(c)
        if s in b:
            b.remove(s)
print(b)


