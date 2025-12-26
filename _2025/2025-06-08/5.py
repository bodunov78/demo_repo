# from sys import *
# from math import *
# from functools import *
# from itertools import *
# from turtle import *
# from fnmatch import *
# # 5 59828
# def tr(n):
#     s=""
#     while n>0:
#         s=str(n%3)+s
#         n=n//3
#     return s
#
#
#
#
# def r(n):
#     s=tr(n)
#     if n%3==0:
#         s=s+s[-3:]
#     else:
#         s=s+tr((n%3)*3)
#
#     return (int(s,3))
#
# mini=[]
# for i in range(1,100):
#     if r(i)>150:
#         mini.append(i)
#         # print (i)
# mini.sort()
# print (mini)