from pickle import *
from random import *
from time import *
ts=time()
# a=[randint(-1000000,1000000) for _  in range(10**7)]
# print (len(a))
# print (time()-ts)
#
# a=[1,2,3]
# with open("p.dat","wb") as f:
#     dump(a,f)
# print (time()-ts)

with open("p.dat","rb") as f2:
    m=load(f2)
print (len(m))
print (time()-ts)
