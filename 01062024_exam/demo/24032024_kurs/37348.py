
#5
from time import *
ts=time()
with open("37348.txt") as f:
    a=[int(x) for x in f]

    cnt=0
    maxi=-10**19
    for i in range(len(a)-1):
        for j in range(i+1,len(a)):
            if a[i]*a[j]%34!=0:
                cnt+=1
                maxi=max(maxi,a[i]+a[j])
    print(cnt,maxi)
print (time()-ts)