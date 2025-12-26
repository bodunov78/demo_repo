from time import *
ts=time()
d7=[[] for x in range(160)]
nd7=[[] for x in range(160)]
maxi=-10**19
cnt=0
with open("37337.txt") as f:
    for x in f:
        x=int(x)
        if x %7==0:
            d7[x%160].append(x)
            d7[x % 160].append(x)

        else:
            nd7[x % 160].append(x)
            nd7[x % 160].append(x)

    for i in range(160):
        for j in range(160):
            if (i !=j ) and len(nd7[i])!=0 and len(d7[j])!=0:
                maxi=max(maxi,max(nd7[i])+max(d7[j]))
                cnt=cnt+len(nd7[i])*len(d7[j])
    for i in range(160-1):
        for j in range(i+1,160):
            if  len(d7[i]) != 0 and len(d7[j]) != 0:
                maxi = max(maxi, max(d7[i]) + max(d7[j]))
                cnt =cnt+len(d7[i])*len(d7[j])
    print(cnt,maxi)
    print(time()-ts)
