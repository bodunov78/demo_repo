from random import *
a=[randint(0,5) for i in range(5)]
print(a)
k=0
for i in range(5):
    k+=a[i]**2
print(k)
