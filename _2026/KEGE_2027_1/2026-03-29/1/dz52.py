from time import *
m=set()
ts=time()
for a in range(1,10_00):
    for b in range(a+1,10_00):
        c=(a**2+b**2)**0.5
        if c%1==0:
            m.add((a,b,int(c)))
print (len(m))
print (time()-ts)