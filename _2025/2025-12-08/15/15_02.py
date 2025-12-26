# from sys import *
# from math import *
# from functools import *
# from itertools import *
# from turtle import *
# from fnmatch import *
#
# def f(x,y,A):
#     return ( (3*x-2*y<A) or (y>=420) or (x>370)   )
#
# for A in range(1000,10000):
#     if all(f(x,y,A) for x in range(1,1000) for y in range(1,1000))==1:
#         print (A)
#         break

#76230
# def f(x,a1,a2):
#     P=  7 <= x  <=68
#     Q = 23<= x <=42
#     A = a1 <= x <=a2
#     return ((not(A)) <=( (Q and P)<=A ))
#
# d=[]
# o=[]
# for x in 7,23,42,68:
#     d.append(x)
#     d.append(x-0.01)
#     d.append(x+0.01)
# for a1 in d:
#     for a2 in d:
#         if all([f(x,a1,a2) for x in range(1,100)]):
#             print (a2-a1)
#             o.append(a2-a1)
# print (min(o))

#34543
# def f(x,a1,a2):
#     P=  3 <= x  <=13
#     Q = 12<= x <=22
#     A = a1 <= x <=a2
#     return ((A) <=( (P or Q) ))
#
# d=[]
# o=[]
# for x in 3,13,12,22:
#     d.append(x)
#     d.append(x-0.01)
#     d.append(x+0.01)
# for a1 in d:
#     for a2 in d:
#         if all([f(x,a1,a2) for x in range(1,100)]):
#             print (a2-a1)
#             o.append(a2-a1)
# print (max(o))
#

# 63064
# def f(x,a):
#     return (((x & 45 > 0) or (x & 89 > 0)) <= (x & a > 0))
#
# for a in range(0, 1000):
#     k = 0
#     for x in range(0, 1000):
#         if f(x,a):
#             k += 1
#     if k == 1000:
#         print(a)
#         break


#60257
#
# def f(x,y,a):
#     return ((x + 2 * y < a) or (y > x) or (x > 60))
# for a in range(0, 300):
#     k = 0
#     for x in range(0, 300):
#         for y in range(0, 300):
#             if f(x,y,a):
#                 k += 1
#     if k == 90_000:
#         print(a)
#         break

