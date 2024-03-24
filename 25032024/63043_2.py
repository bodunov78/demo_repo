#63043
from time import *
ts=time()
with open("63043B.txt") as f:
    k=int(f.readline())
    n = int(f.readline())

    k=3*k

    m=[int(x) for x in f]

    # pr    int (k,m)
    print (time()-ts)
    #CA_B
    maxi=-10**19
    R=[]
    L = []

    C=[max(m[1:k])]


    for i in range(1,len(m)-k):
        if m[i-1]==C[-1]:
            C.append(max(m[i:k+i]))
        elif m[k+i-1]>C[-1]:
            C.append(m[k+i-1])
        else:
            C.append(C[-1])


    print (C[:100])

    maxi = -10 ** 19
    for x in m:
        maxi=max(maxi,x)
        L.append(maxi)

    L.append(-10 ** 19)

    maxi=-10**19
    for x in m[::-1]:
        maxi=max(maxi,x)
        R.append(maxi)
    R=R[::-1]
    R.append(-10**19)

    print (m[:100])
    # print (R)
    # print (L)
        # print (max(m[:i]),m[i],m[i+k])

        # suma=max(suma,max(m[:i])+m[i]+m[i+k])
maxs=-10**19
for i in range(0,len(m)-k):
    maxi=max(L[i-1],R[i+1],C[i])
    maxs=max(maxs,maxi+m[i]+m[i+k])
    print(maxs)


    print (time()-ts)

