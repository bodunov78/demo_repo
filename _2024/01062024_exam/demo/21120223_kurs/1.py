from random import *
K=20
N=10
s={}
for x in range(K):
    m=randint(1,100)
    d=m%N
    if s.get(d):
        s[d].add(m)
    else:
        s[d]={m}
    print (s)

K=20
N=10
s=[[] for x in range(N)]

for x in range(K):
    m=randint(1,100)
    d=m%N
    s[d].append(m)

    print (s)
