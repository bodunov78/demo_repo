# from sys import *
# from math import *
# from functools import *
# from itertools import *
# from turtle import *
# from fnmatch import *
#79732
# def f(s,m):
#     if s>=67 :return m%2==0
#     if m==0: return 0
#     h=[f(s+1,m-1),f(s+4,m-1),f(s*3,m-1)]
#     return any(h) if (m-1)%2==0 else all(h)
#
#
# print ("19",[s for s in range(1,66+1) if not f(s,1) and f(s,2)])
# print ("20",[s for s in range(1,66+1) if not f(s,1) and f(s,3)])
# print ("21",[s for s in range(1,66+1) if not f(s,2) and f(s,4)])

#76234
# def f(s,m):
#     if s<=21 :return m%2==0
#     if m==0: return 0
#     h=[f(s-3,m-1),f(s-7,m-1),f(s//4,m-1)]
#     return any(h) if (m-1)%2==0 else all(h)
#
# ### minimal'no
# print ("19",[s for s in range(100,22-1,-1) if not f(s,1) and f(s,2)])
# print ("20",[s for s in range(100,22-1,-1) if not f(s,1) and f(s,3)])
# print ("21",[s for s in range(100,22-1,-1) if not f(s,2) and f(s,4)])

#
# # 68520
# def f(s,t,m):
#     if s+t>=59 :return m%2==0
#     if m==0: return 0
#     h=[f(s+1,t,m-1),f(s*2,t,m-1),f(s,t+1,m-1),f(s,t*2,m-1)]
#     return any(h) if (m-1)%2==0 else all(h) # else any(h) неудачный ход для 19 / else all(h) для любого хода
#
#
# print ("19",[s for s in range(1,53+1) if not f(s,5,1) and f(s,5,2)])
# print ("20",[s for s in range(1,53+1) if not f(s,5,1) and f(s,5,3)])
# print ("21",[s for s in range(1,53+1) if not f(s,5,2) and f(s,5,4)])
