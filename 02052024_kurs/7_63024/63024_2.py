#Сколько существует 11-значных девятеричных чисел, в записи которых не встречается цифра 0,
# любые две соседние цифры имеют разную чётность, и никакая цифра не повторяется больше 4 раз?
from time import *
ts=time()
c1 = '1357'
c2 = '2468'
count = 0

for i in range(10**11,10**12):
    s=str(i)



print (time()-ts)