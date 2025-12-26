from itertools import *
from time import *

def fu0():

    count = 0
    m = []
    for p in product(sorted("ТЕРМИН"), repeat=10):
        count += 1
        if count % 3 == 0 and p.count("Т") == 1 and (p[0] == 'Е' or p[0] == 'И'):
            m.append(count)
    print(len(m))

def fu00():

    count = 0
    m = []
    for p in product(sorted("ТЕРМИН"), repeat=10):
        count += 1
        if (p[0] in 'Е' or p[0] == 'И') and count % 3 == 0 and p.count("Т") == 1 :
            m.append(count)
    print(len(m))


def fu000():

    count = 0
    m = []
    a=0
    for p in product(sorted("ТЕРМИН"), repeat=10):
        count += 1
        if (p[0] in 'ЕИ') and count % 3 == 0 and p.count("Т") == 1 :
            a+=1
            m.append(count)
    print(len(m),a)



def fu1():
    cnt = 0  # счетчик кол-ва
    kn = 0  # счетчик номера кода в списке
    a = product('ЕИМНРТ', repeat=10)
    for i in a:
        p = ''.join(i)
        kn += 1
        if (p[0] in 'ЕИ') and p.count('Т') == 1 and kn % 3 == 0:
            cnt += 1
    print(cnt)

def fu2():
    s0="ЕИ"
    s1="ЕИМНРТ"
    kn=0
    cnt=0
    for i in product(s0,s1,s1,s1,s1,s1,s1,s1,s1,s1):
        p = ''.join(i)
        kn += 1
        # print (p)

        if  p.count('Т') == 1 and kn % 3 == 0:
            cnt += 1
            # print(p,cnt)
    print(cnt)

def fu3():
    s0="ЕИ"
    s1="ЕИМНРТ"
    kn=0
    cnt=0
    for i in product(s0,s1,s1,s1,s1,s1,s1,s1,s1,s1):
        p = ''.join(i)
        kn += 1
        # print (p)

        if  kn%3==0 and p.count('Т') == 1:
            cnt += 1
            # print(p,cnt)
    print(cnt)

ts=time()
fu2()
print(time()-ts)
