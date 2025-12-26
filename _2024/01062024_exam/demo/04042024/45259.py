#Среди натуральных чисел, не превышающих 109, найдите все числа, соответствующие маске 12345?7?8, делящиеся на число 23 без остатка.

from time import *
from fnmatch import *
ts=time()
for i in range(10):
    for j in range(10):
        n=int(f"12345{i}7{j}8")
        if n%23==0:
            print(n,n//23)
print(time()-ts)

ts=time()

for i in range(123450708,123460000):
    if (i%23==0) and (i%10==8) and ((i//100)%10==7):
        print(i, i//23)
print(time()-ts)


ts=time()

for x in range(0,10**9,23):
    if fnmatch(str(x), '12345?7?8'):
        print(x, x//23)
print(time()-ts)
