#Определите количество четырехзначных чисел, записанных в десятичной системе счисления,
# в записи которых все цифры различны и никакие две чётные и две нечётные цифры не стоят рядом.


# permutations - перестановки (исключает повторений)
from time import *
ts=time()
from itertools import *
s=(0,1,2,3,4,5,6,7,8,9)
cnt=0
for m in permutations(s,4):
    # print (m)
    if  m[0]!=0 and m[0] % 2 == m[2] % 2 and m[0] % 2 != m[1] % 2 and m[1] % 2 == m[3] % 2:
        cnt += 1
        print(m, cnt)

print (time()-ts)