from math import *
def deli(n):
    d=[]
    # print (n)
    for i in range(17,n,10):
        # if n%i==0 and i%10==7 and i!=7:
        if n % i == 0 :

            d.append(i)
            

    # print (d)
    if len(d)>0:
        return d
    else:
        return 0


cnt=0
for i in range(1125000,1325000):

    # print (i)
    if deli(i):
        cnt+=1
        print (i,min(deli(i)))
    if cnt==5:
        break



