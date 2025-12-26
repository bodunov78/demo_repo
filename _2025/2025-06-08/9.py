# from sys import *
# from math import *
# from functools import *
# from itertools import *
# from turtle import *
# from fnmatch import *
# # cnt=0
# # with open("9.txt") as f :
# #     for x in f:
# #         x=x.strip()
# #         # print (x)
# #
# #         m=list(map(int,x.split()))
# #         ind=[m.count(i) for i in set(m)]
# #         ind.sort()
# #         # print (ind)
# #         if ind==[1,1,2,3]:
# #             p=[x for x in m if m.count(x)>1]
# #             np = [x for x in m if m.count(x) ==1]
# #             if sum(p)/len(p) > sum(np)/len(np):
# #                 cnt+=1
# #     print(cnt)
#
#
#
# #76112
# cnt=0
# a=[]
# with open("9_1.txt") as f :
#     for x in f:
#         cnt+=1
#         x=x.strip()
#         # print (x)
#
#         m=list(map(int,x.split()))
#         ind=[m.count(i) for i in set(m)]
#         ind.sort()
#
#         # print (ind)
#         if ind==[1,1,1,1,3]: # 4 различных и 3 повторяющихся
#             p=[x for x in m if m.count(x)>1] # повторяющиеся
#             np = [x for x in m if m.count(x) ==1] # неповторяющиеся
#
#             if sum(np)/len(np) <= sum(p)/len(p) and max(m)%min(m)!=0:
#                 a.append([sum(m),cnt])
#
#     print(max(a))