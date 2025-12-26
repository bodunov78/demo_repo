














































# 01
# from sys import *
# from math import *
# from functools import *
# from itertools import *
# from turtle import *
# from fnmatch import *
# # 1 76216
#
# t="12,16,23,24,26,27,28,37,45,47,58,68"
# g="ЕГ,ЕВ,ВГ,ВА,АГ,ГБ,ГД,ГИ,БД,ДИ,ИЖ,ЖЕ"
# t=t+','+t[::-1]
# g=g+','+g[::-1]
#
# s="АБВГДЕЖИ"
#
# for ss in permutations(s):
#     nt=g
#     for i,v in enumerate(ss):
#         nt=nt.replace(v,str(i+1))
#     if set(nt.split(','))==set(t.split(',')):
#         print (ss)
#
#
#
# # 2 69907
#
# t="13,18,25,28,34,36,46,57,67,78"
# g="DE,EA,EB,AH,HC,HG,CF,FG,GB,BD"
# t=t+','+t[::-1]
# g=g+','+g[::-1]
#
# s="ABCDEFGH"
#
# for ss in permutations(s):
#     nt=g
#     for i,v in enumerate(ss):
#         nt=nt.replace(v,str(i+1))
#     if set(nt.split(','))==set(t.split(',')):
#         print (ss)


# 02
# from sys import *
# from math import *
# from functools import *
# from itertools import *
# from turtle import *
# from fnmatch import *
#
# # 3 79715
# def f(x,y,z,w):
#     return (( x and (not(y)) ) or (y==z)   or (w))
#
#
#
# for a1,a2,a3,a4 in product([0,1], repeat=4):
#     tab=[(a1,a2,1,a3),(1,0,0,0),(1,0,a4,1)]
#
#     if len(set(tab))==len(tab):
#         for p in permutations('xyzw'):
#             if [f(**dict(zip(p,r))) for r in tab] == [0,0,0]:
#                 print (p)
#
#


# 05
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


# 06
# from sys import *
# from math import *
# from functools import *
# from itertools import *
# from turtle import *
# from fnmatch import *
#
# #72591
# screensize(5000,5000)
# k=20
# tracer(0)
#
# for i in range(2):
#     fd(24*k)
#     rt(90)
#     fd(10*k)
#     rt(90)
# up()
#
# fd(3*k)
# lt(90)
# fd(13*k)
# rt(90)
# down()
#
#
# for i in range(2):
#     fd(9*k)
#     rt(90)
#     fd(32*k)
#     rt(90)
#
# up()
# for x in range(-20,50):
#     for y in range(-50,50):
#         goto(x*k,y*k)
#         dot(3,"red")
# done()
#
#

# 09
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

# 13
# from sys import *
# from math import *
# from functools import *
# from itertools import *
# from turtle import *
# from fnmatch import *
#
# from ipaddress import *
# for x in ip_network("48.167.83.95/255.248.0.0",0):
#     print (x)


# 69922
# from ipaddress import *
# net = ip_network(f'112.160.0.0/255.240.0.0', 0)
# cnt = 0
# for ip in net:
#     s = f'{ip:b}'
#     if s.count('1') % 5 != 0:
#         cnt += 1
# print(cnt)

#
#
# from ipaddress import *
# net = ip_network(f'112.160.0.0/255.240.0.0', 0)
# cnt = 0
# for ip in net:
#     s = bin(int(ip))[2:].zfill(32)
#     if s.count('1')%5!=0:
#         cnt+=1
#     # print (s)
# #
# #     if s.count('1') % 5 != 0:
# #         cnt += 1
# print(cnt)

# 15
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

# 76230
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

# 34543
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


# 60257
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


# 16
# from sys import *
# from math import *
# from functools import *
# from itertools import *
# from turtle import *
# from fnmatch import *

# #47220
#
# @lru_cache(None)
# def f(n):
#     if n==1: return 1
#     return n*f(n-1)
#
# for i in range(2,2025,1):
#     f(i)
#
# i= (f(2023)/f(2020))
# print (i)


# #60258
# @lru_cache(None)
# def f(n):
#     if n>2024: return n
#
#     return n*f(n+1)
#
#
# for i in range(2030,-1,-1):
#     f(i)
#
# i= (f(2022)/f(2024))
# print (i)


# 19
# from sys import *
# from math import *
# from functools import *
# from itertools import *
# from turtle import *
# from fnmatch import *
# 79732
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

# 76234
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


# 23
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

# 76238
# def f(s, e,st=''):
#     if s > 22 or st[-2:] == '22':
#         return 0
#     if s == e:
#         return 1
#     return f(s+1,e ,st+'1') + f(s+2,e ,st+'2') + f(s*2, e,st+'3')
# print(f(2,22))


# 72581
# def f(s, e):
#     if s < e:
#         return 0
#     if s == e:
#         return 1
#     else:
#         return f(s - 2, e) + f(s // 2, e) + f(s // 3, e)
# print(f(40, 20) * f(20, 4))

# 24

# from sys import *
# from math import *
# from functools import *
# from itertools import *
# from turtle import *
# from fnmatch import *
# максимальная строка содержащая 85 последовтельностей GSW
# with open("1004_24.txt") as f :
#     s=f.readline().strip()
#     m=85*3
#     maxi=m
#     for l in range(len(s)):
#         for r in range(l+m,len(s)):
#             ss=s[l:r+1]
#             if ss.count('GSW')==85 and ss[-3:]=='GSW':
#                 maxi=max(maxi,len(ss))
#                 m=maxi
#             elif ss.count('GSW')>85:
#                 break
#     print (maxi)

# минимальная длина строки содержащая 130 RSQ и не заканчивающаяся на Q
# with open("24_21717.txt") as f:
#     s=f.readline()
#     m = 10000
#     for l in range(len(s)):
#         for r in range(l + m, l, -1):
#             c = s[l:r + 1]
#             if c.count('RSQ') >= 130 and c[-1]!='Q':
#                 m = min(m, len(c))
#             else:
#                 break
#     print(m)

# 25
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

# 27

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
