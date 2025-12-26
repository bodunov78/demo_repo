#45259
from fnmatch import *
# for x in range(0,10**9,23):
#     if fnmatch(str(x), '12345?7?8'):
#         print(x, x//23)

for i in range(123450708,123460000):
    if (i%23==0) and (i%10==8) and ((i//100)%10==7):
        print(i, i//23)

print("#59918")

from fnmatch import *
sd = []
for i in range (1,20):
    sd.append(2**i)
for x in range(0, 10**9, 31*2031):
    if fnmatch(str(x), '*31*65?'):
        delitel = []
        for i in range(1, round (x**0.5) + 1):
            if x%i==0:
                delitel.append(i)
                delitel.append(x // i)
        if len(delitel) in sd:
            print(x, x // 2031)


#27857
maxi = 0
for i in range(84052, 84131):
    numdel = 0
    for j in range(1, i + 1):
        if i % j == 0:
            numdel += 1
    if numdel > maxi:
        maxi = numdel
        mini = i
print(maxi, mini)

