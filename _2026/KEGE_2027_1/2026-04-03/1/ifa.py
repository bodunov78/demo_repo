from time import *
ts=time()
arr=[]
for a in range(1,10000):
    for b in range(a+1,10000):
        c=int((a**2+b**2)**0.5)
        if a**2+b**2== c**2:
            arr.append((a,b,c))
print (len(arr))
print (time()-ts)