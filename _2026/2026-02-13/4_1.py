from itertools import permutations

l="ЕЗНОР"
s="НЕВЕЗЕНИЕ"
di={'А':3,'В':3,'И':2,}

for c in set(l):
    di[c]=s.count(c)
print (di)


m=[3,3,3,4,4]
k=[]
for a in permutations(set(s)):
    suma=0
    print (a)
    for i,v in enumerate(a):
        # print (m[i],di[v])
        suma+=m[i]*di[v]
    k.append((suma,a))
print (min(k))





