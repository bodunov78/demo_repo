from math import *
def fi(n):
    s=""
    while n>0:
        s=str(n%5)+s
        n=n//5
    return s
a=[]
for x in range(4001):
    if fi(5**100-x).count('0')==4:
        a.append(x)

print (max(a))
