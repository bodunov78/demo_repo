#63043
from time import *
ts=time()
with open("63043C.txt") as f:
    k = int(f.readline()) * 1
    n = int(f.readline())
    a = [int(i) for i in f]
    cnt=0
    maxi = -10 ** 10
    summa = [(a[i] + a[i + k], i, i + k) for i in range(n - k)]
    summa.sort(reverse=0)
    summa=[(100, 1, 4), (100, 2, 5), (100, 0, 4)]
    print(summa,n)
    for i in range(n):
        for j, t, p in summa:
            cnt+=1

            if i != t and i != p:
                maxi = max(maxi, a[i] + j)
                print(i, maxi,cnt)
                break
    print(maxi,cnt)
    print (time()-ts)

