#63043
from time import *
ts=time()
with open("63043B.txt") as f:
    k=int(f.readline())
    k=3*k
    m=[int(x) for x in f]
    # print (k,m)
    print (time()-ts)
    #CA_B
    maxi=max(m[0+1:k])
    for i in range(1,len(m)-k):

        if m[k+i]>maxi:
            maxi=m[k+i]
        if m[i-1] ==maxi:
            maxi = max(m[i:i+k])

    print(time()-ts)
