from itertools import permutations

l="ЕЗНОР"
s="НЕВЕЗЕНИЕ"
di={'А':3,'В':3,'И':2,}
k=set(set(s) -di.keys())

k=["A","Б","В"]
m=[1,2,3]


d=zip(m,k)
# di.update(d)
print (dict(d))
# m=sum([di[x] for x  in s])
# print (m)




