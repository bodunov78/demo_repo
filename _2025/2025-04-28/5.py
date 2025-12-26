# 20:48
def tr(x):
    s=""
    while x>0:
        s=str(x%3)+s
        x=x//3
    return(s)

a=[]
for n in range(10000,1,-1):
    r=tr(n)
    if n%3==0:
        r=r+r[-2:]
    else:
        m=sum(int(x) for x in str(r))
        r=r+tr(m)
    r=int(r,3)
    if r>220:
        a.append(r)
    if n==11 or n==12:
        print(n,r)
print (min(a))

from itertools import *
#20:56
