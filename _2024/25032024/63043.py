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
    suma=-10**19
    for i in range(1,len(m)-k):
        # print (max(m[:i]),m[i],m[i+k])
        suma=max(suma,max(m[:i])+m[i]+m[i+k])
    print (suma)
    print (time()-ts)
    # A_B C
    m=m[::-1]
    for i in range(1, len(m) - k):
        # print(max(m[:i]), m[i], m[i + k])
        suma = max(suma, max(m[:i]) + m[i] + m[i + k])
    print(suma)
    print (time()-ts)
    # A_ C _B
    m = m[::-1]
    for i in range(0, len(m) - k):
        # print(max(m[i+1:i+k]), m[i], m[i + k])
        suma = max(suma, max(m[i+1:i+k])+ m[i]+ m[i + k])
    print(suma)

    print (time()-ts)