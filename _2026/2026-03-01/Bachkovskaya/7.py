from random import *
a=[randint(10,100) for i in range(5)]
print(a)
print(sum(a))
b=sum(a)
for i in range(5):
    c=(a[i]//10)+(a[i]%10)
    d=a[i]%c
    a[i]=d
print(a)
