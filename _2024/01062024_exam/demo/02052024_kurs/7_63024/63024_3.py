#Сколько существует 11-значных девятеричных чисел, в записи которых не встречается цифра 0,
# любые две соседние цифры имеют разную чётность, и никакая цифра не повторяется больше 4 раз?
from time import *
ts=time()
c1 = '1357'
c2 = '2468'
count = 0

for a1 in c1:
    for a2 in c2:
        for a3 in c1:
            for a4 in c2:
                for a5 in c1:
                    for a6 in c2:
                        for a7 in c1:
                            for a8 in c2:
                                for a9 in c1:
                                    for a10 in c2:
                                        for a11 in c1:
                                            s=a1+a2+a3+a4+a5+a6+a7+a8+a9+a10+a11
                                            m=[s.count(x) for x in set(s)]
                                            if max(m)<5:
                                                count+=1

                                                # print (s)
print (count*2)

print (time()-ts)