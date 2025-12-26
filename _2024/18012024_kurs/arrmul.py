from itertools import *
a=[1,2,4]
b=[3,5,7]
s=0
for x,y in list(zip(a,b)):
    s+=x*y
print (s)
#
bn=b[:]
c=[sum([m*n for m,n in zip(a,b)])]
print (c)
#
c=[[m*n for m,n in zip(a,b)] for b in permutations(bn)]
print (c)
#
c=[sum([m*n for m,n in zip(a,b)]) for b in permutations(bn)]
print (c)
#
 c=[sum(map(lambda x,y:x*y,a,b)) for b in permutations(b)]
 print (c)
#
#
# k=[a[:i]+a[i+1:]+[a[i]+1,a[i]+1 ] for i in range(len(a))]
# print (k)
#
#
