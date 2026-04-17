from itertools import *

t="12,14,24,26,34,35,45,46"
g="dc,db,de,cb,eb,ba,bg,ag"

t=t+","+t[::-1]
g=g+","+g[::-1]
# print (t)
# print (g)
L=g.replace(',','')
L=set(L)
# print (L)
L="abcdeg"
for p in permutations(L):
    nt=g
    for i,v in enumerate(p,1):
        nt=nt.replace(v,str(i))

    if set(nt.split(',')) == set(t.split(',')):
        print (p)
