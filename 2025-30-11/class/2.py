# В текстовом файле 2.txt находится цепочка из символов латинского
# алфавита A, B, C, D, E, F.
# Найдите длину самой длинной подцепочки, состоящей из символов A, B, E, F
# (в произвольном порядке).

from string import *

with open("2.txt") as f:
    s=f.readline()
    s=s.strip()
    ss=set(s)
    d=set("ABEF")
    smd=ss-d
    for c in smd:
        s=s.replace(c,':')

    a=[(len(x),x) for x in s.split(':')]
    print (max(a))
