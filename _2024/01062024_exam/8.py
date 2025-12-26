#59746
# Сколько существует десятичных чисел, которые делятся на 5, при условии что все цифры числа различные?
from itertools import *
s="0123456789"
m=[]
for y in range(1,11):
    for x in permutations(s,y):
        if x[-1] == '0' or x[-1] == '5':
            x=int("".join(x))
            m.append(x)

print (len(set(m)))


#59741
# Сколько существует чисел, восьмеричная запись которых содержит 5 цифр, причем в записи нет цифры 1.
# Также все цифры записи различны и никакие две чётные и две нечётные цифры не стоят рядом.

from itertools import *
s="0234567"
m=[]
for x in permutations(s,5):
    k=[str(int(n)%2) for n in x]
    k="".join(k)
    if '11' not in k and '00' not in k and x[0]!='0':
        y=int("".join(x))
        m.append(x)

print (len(set(m)))

#59744
# Евгений составляет 6-буквенные слова из букв М, У, Ж, Ч, И, Н, А. Каждая из букв может встречаться в слове ровно один раз,
# причём первой буквой не может быть Ч, буква Ж должна встречаться не менее 1 раза и номер слова должен быть нечётный.
#
# Сколько различных слов может составить Евгений?

s0="МУЖИНА"
s1="МУЖЧИНА"
cnt=0
cnt1=0
for x in product(s1,s1,s1,s1,s1,s1,s1):
    cnt+=1
    if cnt%2 ==1 and x[0]!='Ч' and x.count('М')==1 and x.count('У')==1 and x.count('Ж')>=1 and x.count('Ч')==1 and  x.count('И')==1 and  x.count('Н')==1 and x.count('А')==1:
        cnt1+=1
        print(x,cnt,cnt1)

#35466
s="ВЕРОНИКА"
s=sorted(s)
print (s)
cnt=0
for x in product(s,repeat=3):
    if x.count('В')==1:
        cnt+=1
        print(x,cnt)
        if x.count('А')==0:
            print (x,cnt)
            break
