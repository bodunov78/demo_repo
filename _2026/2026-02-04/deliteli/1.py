from math import *
from time import *
ts=time()
n=(2**5)*(3**3)*(5**5)*(11**5)*(7**4)
# n=16
d=[]
for i in range(2,ceil(n**0.5)+1):
    if n%i ==0 :
        d.append(i)
        d.append(n//i)
        # print (d)
d=set(d)
print (len(d))
print (time()-ts)
