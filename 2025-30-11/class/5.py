# Текстовый файл 5.txt состоит не более чем из 106 символов
# и содержит только заглавные буквы латинского алфавита и цифры.
# Определите максимальную длину подстроки, в которой ни одна буква не стоит рядом с буквой
# и ни одна цифра не стоит рядом с цифрой.
from string import *
with open("5.txt") as f:
    s=f.readline()
    s=s.strip()
    print (len(s))
    print (s[:100])
    a=printable[10:36].upper()
    print (a)
    d=printable[0:10]
    print (d)
    for c in a:
        s=s.replace(c,'A')
    for c in d:
        s = s.replace(c, '1')

    print (s[:100])
    while 'AA' in s or '11' in s:
        s=s.replace('AA','A:A').replace('11','1:1')
    m=s.split(':')
    print (len(max(m,key=len)))

