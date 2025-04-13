from random import *
a=[randint(1,20) for x in range(10)]
print (a)
print (list(zip(a,a[1:],a[2:])))
for x,y,z in zip(a,a[1:],a[2:]):
    print (x,y,z)

