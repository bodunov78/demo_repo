from time import *
ts=time()
with open("36000.txt") as f:
    n=f.readline()
    m=[]
    ch=[]
    nch=[]
    cnt=0
    maxi=-10**19
    for x in f:
        x=int(x)
        if x%2==0:
            ch.append(x)
        else:
            nch.append(x)
    ch=set(ch)
    nch=set(nch)
    for x in ch:
        for y in nch:
            if (x+y) in nch:
                cnt+=1
                maxi=max(maxi,x+y)
                print (cnt,maxi,x,y,x+y,)

print (time()-ts)