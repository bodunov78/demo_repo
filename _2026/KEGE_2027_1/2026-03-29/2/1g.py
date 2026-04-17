
from random import *
with open ("b.txt","w") as f:

    for  i in range(1000):
        k=randint(1,1000)
        for l in range(k):
            j=randint(0,5)
            n=randint(-10000,10000)
            if j==0:
                print (n,end="\t",file=f)
            else:
                print (n/10**j,end="\t",file=f)
        print("",file=f)