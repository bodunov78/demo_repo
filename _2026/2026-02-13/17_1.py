a=[]
with open("17.txt") as f:
    for s in f:
        a.append(int(s))
print (a)

b=[int(x) for x in open("17.txt")]
print (b)

# for a1,a2,a3 in zip(a,a[1:],a[2:]):
#     print (a1,a2,a3)

# for a1 in range(len(a)):
#     for a2 in range(a1+1,len(a)):
#         for a3 in range(a2+1,len(a)):
#             print (a1,a2,a3)
from itertools import *
for a1,a2 in combinations(a,2):
    print (a1,a2)




