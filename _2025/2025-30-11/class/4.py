# Текстовый файл 4.txt состоит не более чем из 106 символов и содержит
# только заглавные буквы латинского алфавита и цифры.
# Определите максимальную длину подстроки, в которой ни одна буква не стоит рядом
# с буквой и ни одна цифра не стоит рядом с цифрой.

from string import *


with open("3.txt") as f:
    s=f.readline()
    s=s.strip()
    dd=printable[:10]
    ss=printable[10:36].upper()
    # print (d)

    for c in ss:
        s=s.replace(c,'A')

    for c in dd:
        s=s.replace(c,'1')

    while 'AA' in s or '11' in s:
        s=s.replace('AA','A:A').replace('11','1:1')

    a=[(len(x),x) for x in s.split(':')]
    print (max(a))
