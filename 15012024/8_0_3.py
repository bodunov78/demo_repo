from itertools import *
from time import *
#Тип 8 26982

ts=time()
ch0=(0,2,4,6,8,)
ch=(2,4,6,8)
nch=(1,3,7,9)

d=0
for x in product(ch,nch,ch0,nch,ch0,nch,ch0,(5,)):
    if len(x)==len(set(x)):
        # print (x)
        d+=1

nch=(1,3,5,7,9)

for x in product(nch,ch,nch,ch,nch,ch,nch,(0,)):
    if len(x)==len(set(x)) :
        # print (x)
        d+=1

print (d,time()-ts)
