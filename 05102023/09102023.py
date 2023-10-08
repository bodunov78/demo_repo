from itertools import *
from fnmatch import *

# 59713
# Составляют 5-буквенные слова из букв слова ПЯТНИЦА.
# Найти количество слов, которые не начинаются с Н и в которых есть только одна буква Я. Буквы в слове могут повторяться.

def fu11():
    s = "ПЯТНИЦА"
    cnt = 0
    for x1 in s:
        for x2 in s:
            for x3 in s:
                for x4 in s:
                    for x5 in s:
                        x = x1 + x2 + x3 + x4 + x5
                        if x[0] != 'Н' and x.count('Я') == 1:
                            cnt += 1
    print(cnt)

def fu12():
    cnt=0
    s = "ПЯТНИЦА"
    for x in product(s,repeat=5):
        if x[0] != 'Н' and x.count('Я')==1:
            cnt+=1
    print(cnt)

def fu13():
    cnt = 0
    s = "ПЯТНИЦА"
    m=[x1+x2+x3+x4+x5 for x1 in s if x1 !='Н' for x2 in s for x3 in s for x4 in s for x5 in s if (x1+x2+x3+x4+x5).count('Я')==1]
    print(len(m))


def fu14():
    cnt = 0
    s = "ПЯТНИЦА"
    m=[x for x in product(s,repeat=5) if x[0]!='Н' and x.count('Я')==1]
    print(len(m))



# 59745
# Все 5-буквенные слова, в составе которых могут быть буквы А, Л, Г, О, Р, И, Т, М, записаны в алфавитном порядке
# и пронумерованы начиная с 1.
# Определите в этом списке количество слов с нечетными номерами,
# которые не начинаются с буквы Г и при этом содержат в своей записи не менее двух букв И.

def fu21():
    s = "АГИЛМОРТ"
    cnt = 0
    ch=0
    for x1 in s:
        for x2 in s:
            for x3 in s:
                for x4 in s:
                    for x5 in s:
                        x = x1 + x2 + x3 + x4 + x5
                        cnt+=1
                        if x[0] != 'Г' and x.count('М') >= 2 and cnt%2==1:
                          ch+=1

    print(ch)

def fu22():
    s = "АЛГОРИТМ"
    s=sorted(s)
    cnt = 0
    ch=0
    for x1 in s:
        for x2 in s:
            for x3 in s:
                for x4 in s:
                    for x5 in s:
                        x = x1 + x2 + x3 + x4 + x5
                        cnt+=1
                        if x[0] != 'Г' and x.count('М') >= 2 and cnt%2==1:
                          ch+=1

    print(ch)


def fu23():
    cnt=0
    ch=0
    s = sorted("АЛГОРИТМ")
    for x in product(s,repeat=5):
        cnt+=1
        if x[0] != 'Г' and x.count('М')>=2 and cnt%2==1:
            ch+=1
    print(ch)


def fu24():
    cnt=0
    ch=0
    s = sorted("АЛГОРИТМ")
    for x in product(s,repeat=5):
        cnt+=1
        if cnt%2 ==1:
            if x[0] != 'Г' and x.count('М')>=2:
                ch+=1
    print(ch)



# 59831
# Игорь составляет пятизначные числа, используя цифры девятеричной системы счисления.
# Сколько различных чисел может составить Игорь, в которых только одна цифра 5 и рядом с ней НЕ стоят нечётные цифры?


def fu31():
    cnt = 0
    ch=0
    s = "012345678"
    m=["".join(x) for x in product(s,repeat=5)  if x.count('5')==1 and x[0]!='0']
    print(len(m))
    for i,x in enumerate(m):
        for y in ('15','35','75','51','53','57'):
            if y in x:
                m[i]='99999'
                break

    print(m.count('99999'),len(m),len(m)-m.count("99999"))

def fu32():
    cnt = 0
    ch=0
    s = "012345678"
    excl = ["".join(x) for x in product("1357", repeat=2) if x.count('5') == 1]


    m=["".join(x) for x in product(s,repeat=5)  if x.count('5')==1 and x[0]!='0' and all( y not in "".join(x) for y in excl )]
    print (len(m),m)


def fu33():
    cnt = 0
    ch = 0
    s = "012345678"
    excl = ["".join(x) for x in product("1357", repeat=2) if x.count('5') == 1]


    m = ["".join(x) for x in product(s, repeat=5) if x.count('5') == 1 and x[0] != '0' ]
    for y in m:
        if fnmatch(y,'5[0,2,4,6,8]*'):
            print(y)
            cnt+=1
        elif fnmatch(y,'*[0,2,4,6,8]5[0,2,4,6,8]*'):
            print(y)
            cnt += 1
        elif fnmatch(y,'*[0,2,4,6,8]5'):
            print(y)
            cnt += 1

    print(cnt)

def fu34():
    cnt = 0
    s = "012345678"
    m = ["".join(x) for x in product(s, repeat=5) if x.count('5') == 1 and x[0] != '0' ]
    for y in m:
        if fnmatch(y,'5[0,2,4,6,8]*') or fnmatch(y,'*[0,2,4,6,8]5[0,2,4,6,8]*') or fnmatch(y,'*[0,2,4,6,8]5'):
            print(y)
            cnt+=1

    print(cnt)


# fu11()
# fu12()
#fu13()
# fu14()
# fu21()
# fu22()
# fu23()
# fu24()
# fu33()
fu34()