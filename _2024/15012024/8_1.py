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
for var in permutations(kk, 9):

    if var[0] !=0 and (var[-1]%5)==0 and (var[0]%2==var[2]%2==var[4]%2==var[6]%2==var[8]%2) and(var[1]%2==var[3]%2==var[5]%2==var[7]%2):

        count+=1
        # print(var,count)

print(count,time()-st)
