
from random import *
n=10
a=[]
for i in range(10):
    x=[randint(1,99) for s in range(10)]
    a.append(x)

# print (a)


for x in range(10):
    print (*a[x])

s=[x for x in range(12)]

print (s)
m=3
n=4
A = [[0] * m for i in range(n)]
B=[[randint(1,99) for j in range(m)] for i in range(n)]
print (B)

C=[ x  for x in B]

print (sum(C,[]))
print (sum(C))

# for x in B:
#     for y in x:
#         print (y)


