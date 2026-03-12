from random import *
a=[randint(-100,100) for x in range(randint(1,10))]
print(a)
for i in range(len(a)):
    a[i]=a[i]**2

print(a)
