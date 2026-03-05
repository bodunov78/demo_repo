from random import *
a=[randint (11,10000 )for i in range(10)]
print(a)
for i in range(10):
    q=a[i]
    s=0
    while q>0:
        s+=q%10
        q//=10
    a[i]=a[i]%s
print(a)