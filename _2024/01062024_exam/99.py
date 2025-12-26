











































# #номер19-21 (обычный)
# def f(s,m):
#     if s>=43: return m%2==0
#     if m==0: return 0
#     steps=[f(s+1,m-1), f(s+4,m-1), f(s*3,m-1)]
#     return any(steps) if m%2!=0 else all(steps)   #неудачный ход 19 - второе any(steps)!
# print("19", [x for x in range(1,43) if f(x,2)])
# print("20", [x for x in range(1,43) if not f(x,1) and f(x, 3)])
# print("21", [x for x in range(1,43) if not  f(x,2) and f(x,4)])




































#
# #тигра с ограничением:
# def f(s,m):
#     if 36<=s<=60: return m%2==0
#     if s>60: return m%2!=0
#     if m==0: return 0
#     steps=[f(s+1,m-1), f(s+4,m-1), f(s*3,m-1)]
#     return any(steps) if m%2!=0 else all(steps)







































#
# #тигра 2 кучи
# def f(a,b,m):
#     if a+b>=83: return m%2==0
#     if m==0: return 0
#     steps=[f(a+1,b,m-1), f(a*2,b,m-1), f(a,b+1,m-1), f(a, b*2, m-1)]
#     return any(steps) if m%2!=0 else all(steps)
# print("19", [x for x in range(1,74) if f(9,x,2)])
# print("20", [x for x in range(1,74) if not f(9,x,1) and f(9,x, 3)])
# print("21", [x for x in range(1,74) if not  f(9,x,2) and f(9,x,4)])




























#
# #тигра уменьшение
# def f(a,b,m):
#     if a+b<=30: return m%2==0
#     if m==0: return 0
#     steps=[f(a-1,b,m-1), f((a+1)//2,b,m-1), f(a,b-1,m-1), f(a, (b+1)//2, m-1)]
#     return any(steps) if m%2!=0 else all(steps)







































#
# #тигра 3 кучи
# def f(a,b,c,m):
#     if a+b+c>=71: return m%2==0
#     if m==0: return 0
#     steps=[f(a+3,b,c,m-1), f(a*2,b,c,m-1), f(a,b+3,c,m-1), f(a,b*2,c, m-1), f(a,b,c+3,m-1), f(a,b,c*2,m-1)]
#     return any(steps) if m%2!=0 else all(steps)
# print("19", [x for x in range(1,59) if f(7,5,x,2)])
# print("20", [x for x in range(1,59) if not f(7,5,x,1) and f(7,5,x, 3)])
# print("21", [x for x in range(1,59) if not  f(7,5,x,2) and f(7,5,x,4)])







































#
# #второй номер
# from itertools import*
# def f(x,y,w,z):
#     return (наша функция)
# for a1, a2, a3, a4, a5, a6 in product([0,1], repeat=6):
#     str=[(1,a1,a2,a3), (1,1,a4,a5), (1,1,1,a6)]
#     if len(str)==len(set(str)):
#         for k in permutations "xywz":
#             if [f(**dict(zip(k,r))) for r in str]==[0,0,0]:
#                 print(k)






































#
# #2 номер 2 функции
# from itertools import*
# def f1(x,y,w,z):
#     return (.....)
# def f2(x,y,w,z):
#     return (....)
# основа такая же как в обычном
# for k in permutations "xywz":
#     if [f1(**dict(zip(k,r))) for r in str]==[конец функции] and [f2(**dict(zip(k,r))) for r in str]==[конец функции]:
#         print(k)






































#
# #номер 5 с троичным преобразованием
# def f(n):
#     s=""
#     while n>0:
#         s=str(n%3) + s
#         n//=3
#     return s
# c=set()
# for n in range(1,100):
#     s=f(n)
#     if n%3==0:
#         s=s+s[-3:]
#     else:
#         s=s+f((n%3)*3)
#     r=int(s, 3)
#     if r>150:
#         c.add(n)
# print(min(c))







































#
# #9 номер
# f=open("9.zadaniesch.txt") #62515школково
# cnt=0
# for s in f:
#     a=list(map(int,s.split()))
#     a.sort()
#     if len(a)==len(set(a)):
#         if 3*(a[0]+a[-1])<=(a[1]+a[2]+a[3])*2:
#             cnt+=1
# print(cnt)






































#
# #номер 12 с N
# for n in range(4, 100):
#     s="2"+"5"*n
#     while "25" in s or "355" in s or "555" in s:
#         s=s.replace(пишем все что нужно)
#     if 2*s.count("2") + 3*s.count("3") + 5*s.count("5")==17:
#         print(n)
#         break









































#
# #номер 12 с простым числом
# def f(n):
#     for i in range(2, int(n**0.5)+1):
#         if n%i==0:
#             return False
#     return True
# minn=1000000
# for x in range(100):
#     for y in range(100):
#         s="0" + "1"*x + "2"*y
#         if len(s)>40:
#             while "01" in s or "02" in s:
#                 s=s.replace(...)
#             if f(s.count("1") + s.count("2")*2):
#                 minn=min(minn, x+2*y)
# print(minn)
#








































# #номер 14(степени)
# f=49**10 +7**30 -49
# s=""
# while f>0:
#     s=s + str(f%7)
#     f=f//7
# print(s.count("6"))
#






































# #номер 14(одна переменная)
# #19 сс в примере
# for x in "0123456789abcdefghi":
#     x1="78" + x + "79643"
#     x2="25" + x + "43"
#     x3="63" + x + "5"
#     res=int(x1, 19) + int(x2, 19) + int(x3, 19)
#     if res %18==0:
#         res=res//18
#         print(res)
#         break(если наименьшее)








































# #номер 14(две переменные)
# arr=[]
# for x in "0123456":
#     for y in "0123456":
#         t=int(y+x+"320",7)+int("1"+x+"3"+y+"3", 9)
#         if t%181==0:
#             arr.append(t)
# if arr:
#     print(min(arr)//181)
#






































# #номер 14(разные основания)
# arr=[]
# for x in "0123456789ABCDE":
#     t=int("97968" + x + "15", 15) + int("7" + x + "233", 15):
#     if t%14==0:
#         arr.append(t)
# if arr:
#     print(min(arr)//14)
#
#






































# #номер 15(ДЕЛ) (x,a)-> в функ пишем x%a
# #(!= пишем если отрицание)
# for a in range(100,0,-1):
#     k=0
#     for x in range(1,1000):
#         if (x%a!=0) <= ((x%6==0) <= (x%4!=0)):
#             k+=1
#     if k==999:
#         print(a)
#         break(если наименьшее)
#







































# #номер 15(делитель)
# def f(x,a):
#     return (функция)
# for a in range(1,1000):
#     if all(f(x,a) for x in range(1000)):
#         print(a)
#         break
#








































# #номер 15(координатная плоскость)
# for a in range(1000):
#     if all(.....) for x in range(1000) for y in range(1000)):
#         print(A)
#         break
# #15(&&&)
# for a in range(32):
#     b=True
#     for x in range(32):
#         if ((x&25==0) or (x&17!=0) or (x&a!=0))==0:
#             b=False
#     if b:
#         print(a)
#         break
#















































# #15(отрезки)
# p=list(range(10,30+1))
# q=list(range(22,46+1))
# a=[]
# for x in range(1,100):
#     if (...)==False:
#         a.append(x)
# print(a)
#






































# #16 номер границы
# import sys
# sys.setrecursionlimit(10**6)
#
# #17
# f=open(наш файл)
# arr=[int(i) for i in f]
# #ЕСЛИ ПАРЫ ДРУГ ЗА ДРУГОМ
# for i in range(len(arr)-1):
#     arr[i] и тд
# #ЕСЛИ НЕ ПОДРЯД
# for i in range(len(arr)-1):
#     for j in range(i+1, len(arr)):
#         arr[i] + arr[j]
# #ТРОЙКИ
# for i in range(len(arr)-2):
#     arr3=sorted(arr[i], arr[i+1], arr[i+2])
#






































# #25 через фнмэтч
# from fnmatch import*
# for x in range(0,10**10, 1991):
#     if fnmatch (str(x), "наша маска"):
#     print(x, x//1991)