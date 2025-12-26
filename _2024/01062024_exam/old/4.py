import re
from itertools import *
from re import *
from fnmatch import *
from math import *

def new_ard(n):
    a = []
    n=6
    for i in range(1, n + 1):
        # все префиксы, как двоичные числа
        for x in range(2 ** i):
            pfx = bin(x)[2:].zfill(i)
            a.append(pfx)

    print(a)
    return a


def ard(a, r):
    # r=':001'
    a = [x for x in a if not (r in x)]
    for i in range(len(r), 1, -1):
        # print (r[:i])
        a = [x for x in a if x != r[:i]]
    print(len(a), a)
    return a


def ardn(a, r):
    a = [x for x in a if not (x.startswith(r) or r.startswith(x))]
    print("ardn", a)
    return a


def ardm(a):
    a = list(a)

    flag = 1
    for i in range(len(a)):
        for j in range(len(a)):
            if (i != j):
                if a[i].startswith(a[j]) or a[j].startswith(a[i]):
                    # print(i, j)
                    flag = 0
    if flag == 1:
        return a
    else:
        return 0


q = [3, 1,0]

k = new_ard(len(q))
    #Б     #г     #к
s = ['0001','01','001','1110']
bgk=2+3+4
for x in s:
    k = ardn(k, x)

print(k[:3])
summ=10**20
print(factorial(len(k))/factorial(len(k)-len(q)))
if input("Продолжить?:") == 'y':
    l4 = list(combinations(k, len(q)))
    l5 = [a for a in l4 if ardm(a)]
    for z in l5:
        y = [len(c) for c in z]
        suma=0
        if sum(y) < 17:
            for i in range(len(q)): suma=suma+y[i]*q[i]
            summ = min(summ, suma + bgk)
            print(sum(y), y, z,suma+bgk)

# print (l5)

# mina=10**20
# for s in l4:
#     b=[1  for j in s  for i in s  if j in i ]
#
#     if len(b) ==len(q):
#         v = [len(j)-1 for j in s]
#         v.sort()
#         w= [v[i]*q[i] for i in range(len(q))]
#         if mina >= sum(w):
#             mina=min(mina,sum(w))
#             print (s,b,v,w,sum(w),mina)
#
#
# # print (a)
