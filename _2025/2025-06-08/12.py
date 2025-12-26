from sys import *
from math import *
from functools import *
from itertools import *
from turtle import *
from fnmatch import *


for n in range(3,10_000):
    s='4'+'2'*n

    while '42' in s or '8222' in s or '2222' in s:
        s = s.replace('42','2',1)
        s = s.replace('8222', '24', 1)
        s = s.replace('2222', '8', 1)

    suma=sum(int(x) for x in s)
    if suma==40:
        print (n)
        break