# Текстовый файл 3.txt состоит не более чем из 106 символов
# и содержит только заглавные буквы латинского алфавита и цифры. Определите максимальную длину подстроки,
# которая может являться записью числа в шестнадцатеричной системе счисления.

from string import *


with open("3.txt") as f:
    s=f.readline()
    s=s.strip()
    ss=set(s)
    d=set(printable[:16].upper())
    # print (d)
    smd=ss-d
    for c in smd:
        s=s.replace(c,':')

    a=[(len(x),x) for x in s.split(':')]
    print (max(a))
