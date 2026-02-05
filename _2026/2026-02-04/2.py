#59713
from itertools import *
l="ПЯТНИЦА"
l0="ПЯТИЦА"
cnt=0
for a1 in l:
    for a2 in l:
        for a3 in l:
            for a4 in l:
                for a5 in l:
                    s=a1+a2+a3+a4+a5
                    if s[0]!= 'Н' and s.count('Я')==1:
                        print (s)
                        cnt+=1
print (cnt)
cnt=0
for x in product(l,repeat=5):
    print (type(x))
    s="".join(x)
    if s[0] != 'Н' and s.count('Я') == 1:
        print (s)
        cnt+=1
print(cnt)

for x in product("12","35","AB","EF"):
    s = "".join(x)
    print (s)

s="АЛГОРИТМ"
s=sorted(s)
print (s)
cnt=0
for i,v in enumerate(product(s,repeat=5),1):
    v="".join(v)
    if i%2==1 and v[0]!='Г' and v.count('И')>=2:
        cnt+=1
        print (i,v)
print (cnt)

#59745
n=0
cnt=0
for x in product(s,repeat=5):
    n+=1
    x="".join(x)
    if n % 2 == 1 and x[0] != 'Г' and x.count('И') >= 2:
        cnt += 1
        print(i, x)
print(cnt)
