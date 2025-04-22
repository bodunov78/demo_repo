# 13:14
from itertools import *


tab="12,14,24,26,35,36,37,46,47,56,67"
gr="AB,AV,BV,BD,VD,DE,VE,VG,GE,GK,EK"
tab=tab+','+tab[::-1]
gr=gr+','+gr[::-1]

s="ABVGDEK"
for x in permutations(s):
    ntab=gr
    for i,v in enumerate(x):
        ntab=ntab.replace(v,str(i+1))
    if set(tab.split(','))==set(ntab.split(',')):
        print (x)
    # 13:19