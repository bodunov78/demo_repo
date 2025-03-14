
#3
from time import *
ts=time()
with open("37337.txt") as f:
    a=[int(x) for x in f]

    a=a*2
    cnt=0
    maxi=-10**19
    for i in range(len(a)-1):
        for j in range(i+1,len(a)):
            if a[i]%160 != a[j]%160 and (a[i]%7==0 or a[j]%7==0):
                cnt+=1
                maxi=max(maxi,a[i]+a[j])
    print(cnt,maxi)
print (time()-ts)