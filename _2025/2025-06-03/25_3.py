from math import *
def deli(n):
    m=set()
    # print (type(n))
    for i in range(2,ceil(n**0.5)+1):
        if n%i==0:
            m.add(i)
            m.add(n//i)
    # print(sum(m))
    if len(m)>0:
        return min(m)+max(m)
    else:
        return 0


cnt=0
for i in range(800_000,805_000):
    if deli(i)%10==4:
        cnt+=1
        print (i,deli(i))
    if cnt==5:
        break