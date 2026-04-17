from random import *
from time import *
ts=time()
# a=[randint(-1000,1000) for _ in range(10**7)]
# print (a)
a=[]
for _ in range(10**4):
    k=randint(-1000,1000)
    a.append(k)
# print (a)
print (time()-ts)
ts=time()
for i in range(0,len(a)):
    for j in range(i+1,len(a)):
        if a[i]>a[j]:
            a[i],a[j] = a[j],a[i]

# a.sort()
print(time() - ts)

[1, 2, 3 ,5 , 7 , 9, 10, 20, 30, 40, 50]
1000 000
500 000
250 000
125 000
62 000
31 000
15 000
7 000
3500
1800
900
450
225
112
56
28
14
7
4
2
1
0

