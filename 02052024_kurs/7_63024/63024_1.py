#Сколько существует 11-значных девятеричных чисел, в записи которых не встречается цифра 0,
# любые две соседние цифры имеют разную чётность, и никакая цифра не повторяется больше 4 раз?
from time import *
from itertools import *
ts=time()
c1 = '1357'
c2 = '2468'
count = 0
for i in product(c1,c2,c1,c2,c1,c2,c1,c2,c1,c2,c1):
    s = ''.join(i)
    # s=i
    m = [s.count(x) for x in set(s)]
    if max(m) < 5:
    # if s.count('1') < 5 and s.count('2') < 5 and s.count('3') < 5 and s.count('4') < 5 and s.count('5') < 5 and s.count('6') < 5 and s.count('7') < 5 and s.count('8') < 5:
        count += 1
print(count * 2,time()-ts)