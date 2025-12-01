from sys import *
from math import *
from functools import *
from itertools import *
from turtle import *
from fnmatch import *
cnt=0
for s in product('0123456',repeat=5):
    ns="".join(s)
    ns=ns.replace('3','1').replace('5','1')
    if ns.count('6')==1 and ns[0]!='0' and '16' not in ns and '61' not in ns:
        cnt+=1
        print (s,cnt)
