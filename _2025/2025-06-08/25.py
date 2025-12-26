# from sys import *
# from math import *
# from functools import *
# from itertools import *
# from turtle import *
# from fnmatch import *


# for i in range(0,10**10,21453):
#     if fnmatch(str(i),"13?4*7?9"):
#         print (i,i/21453)

# 25 79738
#
# def deli(n):
#     m={1,n}
#
#     for i in range(1,n):
#         if n%i==0:
#             m.add(i)
#             m.add(n//i)
#     # print (m)
#     return sum(m)
# cnt=0
#
# i=500_000
# print (deli(20))
#
# while cnt<6:
#
#     # print (i,deli(i))
#     if deli(i)%10==6:
#         cnt+=1
#         print (i,deli(i))
#
#     i+=1

# 28121

#
# def deli(n):
#
#     a=set()
#
#     for i in range(2,ceil(n**0.5)+1):
#         if n%i==0:
#             return 0
#
#
#     return 1
#
# print (deli(127))
# for i in range(2422000,2422080+1):
#     if deli(i)==1:
#         print (i)