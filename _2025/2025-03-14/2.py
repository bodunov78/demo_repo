#58521
from itertools import *
s="ab,be,bv,vg,vj,vi,gi,db,da,ed,el,ev,je,jm,in,ij,kd,lk,ld,ml,me,mi,nm"

m=s.split(',')
print (m,len(m))
a=set()
for x in range(2,10+1):
    for c in permutations("bvgdejiklm",x):
        c='n'+"".join(c)+'a'
        a.add(c)
# print(a)
for x in a:
    t=[x[i:i+2] in  m  for i in range(len(x)-1)]
    if all(t):
        print (x)

