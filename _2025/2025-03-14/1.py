from itertools import *
s="12,13,14,15,21,23,24,31,32,34,35,42,43,45,51,52,53,54"

m=s.split(',')
print (m)
a=set()
for x in range(2,5+1):
    for c in permutations("12345",x):
        a.add("".join(c))
for x in a:
    t=[x[i:i+2] in  m  for i in range(len(x)-1)]
    if all(t) and x[0]=='1' and x[-1]=='5':
        print (x)

print (a)