#4

from time import *
ts=time()
with open("37359.txt") as f:
    a=[int(x) for x in f]
    cnt=0
    maxi=-10**19
    for i in range(len(a)-1):
        for j in range(i+1,len(a)):
            suma=(a[i]+a[j])
            if suma%117==0:
                cnt+=1
                maxi=max(maxi,suma)
    print(cnt,maxi)
print(time()-ts)