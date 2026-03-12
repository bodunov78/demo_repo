from random import *
c=0
while c !=100:
    a=randint(-100000,0)
    if a%15==0:
        c+=1
        print(a, end=' ')
print()
for i in range(100):
    b=randint(-100000, 0)
    while b%15!=0:
        b = randint(-100000, 0)
    print(b, end=' ')
