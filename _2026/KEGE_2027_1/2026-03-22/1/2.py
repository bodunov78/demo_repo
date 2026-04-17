
from itertools import *
from string import *
cnt=0
for x in product([1,2,3,4],repeat=5):
    if x.count(1)==2:
        cnt+=1
        print (x)
print (cnt)
cnt=0
for x in product((1,2,3),(0,1,2,3),(0,1,2,3)):
    if x[0]+x[-1]>x[1]:
        cnt+=1
        print (x)
print (cnt)

cnt=0
for x in product("ПЯТНИЦА",repeat=5):
    if x[0]!='Н' and x.count('Я')==1:
        cnt+=1
        print(x)
print (cnt)
L=printable[10:36].upper()
print (L)
cnt=0
for l in range(1,6+1):
    for x in product(L,repeat=l):
        cnt+=1
        if "".join(x)=="FDECBA":
            print (x,cnt)