# from sys import *
# from math import *
# from functools import *
# from itertools import *
# from turtle import *
# from fnmatch import *
#
# def f(s,e):
#     if s==e : return 1
#     elif s<e or s==21 : return 0 # не содержит 21
#     else : return (f(s-2,e)+f(s-5,e)+f(s//3,e))
#
# print (f(46,42)*f(42,17)*f(17,4))

#76238
# def f(s, e,st=''):
#     if s > 22 or st[-2:] == '22':
#         return 0
#     if s == e:
#         return 1
#     return f(s+1,e ,st+'1') + f(s+2,e ,st+'2') + f(s*2, e,st+'3')
# print(f(2,22))


#72581
# def f(s, e):
#     if s < e:
#         return 0
#     if s == e:
#         return 1
#     else:
#         return f(s - 2, e) + f(s // 2, e) + f(s // 3, e)
# print(f(40, 20) * f(20, 4))