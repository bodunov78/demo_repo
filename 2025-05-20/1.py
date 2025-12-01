from itertools import *
from fnmatch import *
from functools import *
from math import *
from pickle import *

tab="15,16,17,23,24,28,37,38,47,56,58"
gra="AB,AH,BH,HF,GF,FD,DC,GC,CE,GE,AE"

tab=tab+","+tab[::-1]
gra=gra+","+gra[::-1]


s="ABCDEFGH"

for ss in permutations(s):
    ngra=gra
    for i,v in enumerate(ss):
        ngra=ngra.replace(v,str(i+1))
    if set(tab.split(','))==set(ngra.split(',')):
        print (ss)

print(26)