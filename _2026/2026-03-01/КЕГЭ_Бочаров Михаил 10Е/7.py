from random import *
def f(x):
    k=0
    while x>0:
        k=k+x%10
        x=x//10
    return(k)
a=[randint(10,1000) for i in range(randint(1,20))]
print(a)
for k in range(len(a)):
    a[k]=a[k]%f(a[k])
print(a)
