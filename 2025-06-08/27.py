# from sys import *
# from math import *
# from functools import *
# from itertools import *
# from turtle import *
# from fnmatch import *
#
# # 76439
#
# def centa(clu):
#     c=[]
#     for p1 in clu:
#         suma=0
#         for p2 in clu:
#             suma+=dist(p1,p2)
#         c.append([suma,p1])
#     # print (min(c))
#     return min(c)[1]
#
# with open("27.txt") as f :
#     a=[]
#     # s=f.readline()
#     for x in f:
#         x=x.strip().replace(',','.')
#         # print (x)
#
#         a.append(list(map(float,x.split())))
#         # # a=[list(map(float,x.split())) for x in f]
#     # print (a)
#
#
#     cluster=[]
#     for x in a:
#         cl=[a.pop()]
#         for p1 in cl:
#             sosedi=[p2 for p2 in a if dist(p1,p2)<1]
#             for p2 in sosedi:
#                 if p2 in a:
#                     a.remove(p2)
#                 cl.append(p2)
#         cluster.append(cl)
#
#     # print (cluster)
#     px=0
#     py=0
#     for x in cluster:
#         # print (centa(x))
#         px += centa(x)[0]
#         py += centa(x)[1]
#     # px=  abs((px*10_000/len(cluster))//1) # абсолютное значение целой части
#     # py = abs((py * 10_000 / len(cluster))//1)
#     px=  (abs(px)*10_000/len(cluster))//1   # целая часть абсолютного значения
#     py = (abs(py) * 10_000 / len(cluster))//1
#
#     print (px,py)
#
#
#
