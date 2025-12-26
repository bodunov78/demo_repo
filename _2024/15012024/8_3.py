from itertools import *
from time import *

#Тип 8 26982

st=time()
ch0=(0,2,4,6,8,)
ch=(2,4,6,8)
nch=(1,3,5,7,9)

d=0
kk=(0,1,2,3,4,5,6,7,8,9)

count = 0
for x in range(10000000,100000000,5):
    var=str(x)
    m=set(var)

    if len(m)==8 and var[0]!='0':



        if (int(var[0])%2==int(var[2])%2==int(var[4])%2==int(var[6])%2) and(int(var[1])%2==int(var[3])%2==int(var[5])%2==int(var[7])%2):
            
            count+=1

print(count,time()-st)
