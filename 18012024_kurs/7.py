from itertools import *
b=[2,1,1,0]
x=[[2,2]]
bn=b[:]
# c=[sum([m*n for m,n in zip(a,b)])]
# print (c)

# c=[[m*n for m,n in zip(a,b)] for b in permutations(bn)]

# c=[sum([m*n for m,n in zip(a,b)]) for b in permutations(bn)]
# print (c)

# c=[sum(map(lambda x,y:x*y,a,b)) for b in permutations(b)]
# print (c)
for a in x:
    k = [a[:i] + a[i + 1:] + [a[i] + 1, a[i] + 1] for i in range(len(a))]
#a = set(tuple(x) for x in k)
    print (k)


