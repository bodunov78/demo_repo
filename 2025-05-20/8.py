from itertools import *
from fnmatch import *
from functools import *
from math import *
from pickle import *
from turtle import *

s="012345678"
s0="2468"
s4="1357"
cnt=0
for x in product(s0,s,s,s,s4):
    k="".join(x)
    if k.count('3')==1:
        cnt+=1
        print(k,cnt)