from itertools import permutations

s="КОЛОБОК"
di=dict()
for c in set(s):
    di[c]=s.count(c)
print (di)


m=[2, 3, 3, 3]
   к  л  о  б
   л  к  о  б

k=[]
for a in permutations(set(s)):
    suma=0
    print (a)
    for i,v in enumerate(a):
        # print (m[i],di[v])
        suma+=m[i]*di[v]
    k.append((suma,a))
print (min(k))

1 2 3 1 5 3 2
к о л о б о к

о к л о б о к