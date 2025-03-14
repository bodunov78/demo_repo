#Определите количество четырехзначных чисел, записанных в десятичной системе счисления,
# в записи которых все цифры различны и никакие две чётные и две нечётные цифры не стоят рядом.




















from time import *
ts=time()
cnt=0
for x in range(1000,10000):
    m=str(x)
    if  len(m) == len(set(m)) and int(m[0]) % 2 == int(m[2]) % 2 and int(m[0]) % 2 != int(m[1]) % 2 and (int(m[1]) % 2 == int(m[3]) % 2):
        cnt += 1
        print(m, cnt)

print (time()-ts)