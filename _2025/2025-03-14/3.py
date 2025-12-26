#10389
from itertools import *
s="ab,av,ag,ad,bv,be,ve,ge,dg,de,ek,el,km,kn,lm,ln,mn,np,nr,pr,pt,rt"

m=s.split(',')
print (m,len(m))
a=set()
g=[]
for x in range(2,11+1):
    for c in permutations("bvgdeklmnpr",x):
        c='a'+"".join(c)+'t'
        a.add(c)
# print(a)
for x in a:
    t=[x[i:i+2] in  m  for i in range(len(x)-1)]
    if all(t):
        g.append(x)
        print (x)

print (len(g))