#13:03 _13:13
from itertools import *
tab="16,17,23,24,26,34,45,57,67"
gr="AB,BV,BK,VD,VG,GD,DE,EK,KA"
tab=tab+','+tab[::-1]
gr=gr+','+gr[::-1]

s="ABVGDEK"
for x in permutations(s):
    ntab=gr
    for i,v in enumerate(x):
        ntab=ntab.replace(v,str(i+1))
    if set(ntab.split(','))==set(tab.split(',')):
        print(x,tab,ntab,)



