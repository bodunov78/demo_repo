from itertools import *

s='0123456789'
m=[['0','5']]
for i in range(10):
    n=[]
    nn=[]
    for x in m[-1]:
        for i in s:
            k=i+x
            n.append(k)
                # print (m)
    for v in n:
        if len(v)==len(set(v)):
            nn.append(v)
    m.append(nn)
print (len(m[]))

