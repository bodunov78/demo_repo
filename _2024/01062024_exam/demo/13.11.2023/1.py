from random import *
n=100000
di={}
print (randint(0,36))
while n>0:
    n=n//2
    x=randint(0, 36)
    di[x]=di.get(x,0)+1

print (di)
