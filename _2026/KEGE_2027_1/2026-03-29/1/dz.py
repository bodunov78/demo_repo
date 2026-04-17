from random import *
BIG=set()

while len(BIG)<700:
    BIG.add(randint(0,1000))

print (len(BIG),BIG)
#
S1=set(i for i in range(0,1000+1,2))
S2=set(i for i in range(1,1000,2))
print (S1,len(S1))
print (S2,len(S2))
print (len(BIG&S1))
print (len(BIG&S2))
print (len(BIG-S2))
print (len(BIG-S1))
