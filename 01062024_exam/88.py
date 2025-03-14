# #perevod (2-9)
# def per(chislo, baza):
#     s = " "
#     while chislo > 0:
#         s = str(chislo%baza) + s
#         chislo //= baza
#     return s
#





































# def zad_2():
#     from itertools import *
#     def f(x, y, w, z):
#         return ((x <= y) == (z <= w)) or (x and w) # Сюда пишем функцию
#
#     for a1, a2, a3, a4, a5, a6 in product([0, 1], repeat = 6):
#         stroka = [(1, a1, a2, a3),(1,1, a4, a5),(1, 1, 1, a6)]
#         if len(stroka) == len(set(stroka)):
#             for chtoto in permutations('xywz'):
#                 if [f(** dict(zip(chtoto, r))) for r in stroka] == [0, 0, 0]: # Сюда F
#                     print(chtoto)
#
#






































# def zad_5():
#     for n in range (1,100):
#         d = per(n,2)
#         if n % 3 == 0:
#             r = d + ((d[::-1])[:3])[::-1]
#         else:
#             r = d + str(per(((n % 3) * 3), 2))
#         # print(n, d, r,int(r,2))
#         if int(r,2) > 151:
#             print(int(r,2),r,n)
#             break
#
#
#






































# def zad_6_cherepaha():
#
#     from turtle import *
#     tracer(0)
#     m = 50
#     screensize(2000,2000)
#     left(90)
#
#
#     for i in range(2):
#         forward(8*m)
#         right(90)
#         forward(18 * m)
#         right(90)
#     up()
#     forward(4*m)
#     right(90)
#     forward(10*m)
#     left(90)
#     down()
#     for i in range(2):
#         forward(17*m)
#         right(90)
#         forward(7 * m)
#         right(90)
#
#     up()
#     for x in range(-20,20):
#         for y in range(-20,20):
#             goto(x*m,y*m)
#             dot(5, "blue")
#     done()
#
#






































# def zad_8_1():
#     from itertools import *
#     alf = ""#Алфавит (буквы)
#     cnt = 0
#     n = int(input()) #кол-во букв в слове
#     ansver = []
#     for i in product(alf, repeat = n):
#         a = "".join(i)
#         cnt+= 1
#         if ...... # Условие задачи
#           ansver.append(cnt) #cnt усли номер слова
#         print(max(ansver))
#
#








































# def zad_8_2():
#     from itertools import *
#     cnt = 0
#     alf = ""
#     for i in permutations(alf,len(alf)):
#         a = "".join(i)
#         if ....... # условие
#             cnt += 1
#     print(cnt)
#
#






































# def zad_9():
#     f = open("file")
#     al = []
#     for s in f:
#         al += list(map(int, s.split()))
#     f = open("file")
#     cnt = 0
#     for s in f:
#         b = list(map(int, s.split()))
#         for elements in b:
#             if ....... # условие
#                 cnt += 1
#                 break
#     print(cnt)
#







































# def ipa_andresa():
#     import ipaddress
#     net = ipaddress.ip_network("/")# айпишнник и кол во едениц в маске
#     cnt = 0
#     for ip in net:
#         if bin(int(ip))[2:].count("1")%2 == 0:
#             cnt += 1
#     print(cnt)
#






































# def zad_14():
#     def simple(x):
#         return x == 2 or all(x%d for d in range(2,round(x**0.5)+1))
#     for x in "0123456789ABCDEF"[::-1]:
#         c = int("28"+x+"2",18) + int("93"+x+"5",12)
#         if simple(c):
#             print(c,x)
#             break
#
#
#







































# def otrezki_15():
#     from itertools import *
#     def f(x):
#         P = 25 <= x <= 51
#         Q = 12 <= x <= 37
#         A = a1 <= x <= a2
#         return (P==Q) <= (not A)
#     Ox = [x/4 for x in range(10*4, 60*4)]
#
#     m = []
#     for a1,a2 in combinations(Ox,2):
#         if all(f(x)for x in Ox):
#             m += [a2-a1]
#     print(max(m))
#







































# def zad_16():
#     def f(n):
#         if n == 1:
#             return 1
#         if n > 1:
#             return f(n-1)*f(n+1)
#     print(f(4))
#





































# def kamni_19_20_21():
#     def f(a,b,m):
#         if a+b <= 124: return m%2 == 0
#         if m == 0: return 0
#         h = [f(a-1,b,m-1),f(a-1,b,m-1),f(a-1,b,m-1),f(a-1,b,m-1)] # ходы
#         return any(h) if (m-1)%2 == 0 else any(h) #all 20 21
#
#     print("19: ", [s for s in range(11,1000) if f(10,s,2)])
#     print("20: ", [s for s in range(11,1000) if not (f(10,s,1)) and (f(10,s,3))])
#     print("21: ", [s for s in range(11,1000) if not (f(10,s,2)) and (f(10,s,4))])
#
#






































# def zad_23():
#     def f(n, k):
#         if n > k:
#             return 0
#         if n == k:
#             return 1
#         else:
#             return f(n + 2, y) + f(n * 2, y) + f(n + 3, y)
#     print(f(2, 11) * f(11, 22))
#
#






































# def zad_24_TwoPoints():
#     l = 0
#     cnt = 0
#     min_l = 10**10
#     for r in range(len(s)):
#         if s[r] == "E":
#             cnt += 1
#         while cnt >= 240:
#             if s[l] == "E":
#                 cnt -= 1
#             l+= 1
#             if cnt == 240:
#                 min_l = (min(min_l, r-l+1))
#     print(min_l)
#







































