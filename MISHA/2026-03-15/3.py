a=[1,0,1,1,1,1,2]

from itertools import *
for i in range(len(a)):
    for j in range(i+1,len(a)):
        for k in range(j+1,len(a)):
            for m in range(k+1,len(a)):
                print (a[i],a[j],a[k],a[m])

for x in combinations(a,4):
    print (x)