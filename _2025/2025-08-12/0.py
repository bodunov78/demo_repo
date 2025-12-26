# lst_in = ['8 11 -5', '3 4 10', '-1 -2 3', '-4 5 6']
#
# s="house=дом car=машина men=человек tree=дерево"
# s_lst = s.split()
# l=tuple(tuple(map(str,x.split('='))) for x in s_lst)
# print (l)
# t = {'ё': 'yo', 'а': 'a', 'б': 'b', 'в': 'v', 'г': 'g', 'д': 'd', 'е': 'e', 'ж': 'zh',
#      'з': 'z', 'и': 'i', 'й': 'y', 'к': 'k', 'л': 'l', 'м': 'm', 'н': 'n', 'о': 'o', 'п': 'p',
#      'р': 'r', 'с': 's', 'т': 't', 'у': 'u', 'ф': 'f', 'х': 'h', 'ц': 'c', 'ч': 'ch', 'ш': 'sh',
#      'щ': 'shch', 'ъ': '', 'ы': 'y', 'ь': '', 'э': 'e', 'ю': 'yu', 'я': 'ya'}
# # s=input()
# s="Привет Питон"
# st = "".join(map(lambda x: t[x] if x in t else '-', s.lower()))
#
# print (st)

# s="Москва Уфа Вологда Тула Владивосток Хабаровск"
# st = list((map(lambda x: x if len(x)> 5 else '-', s.split())))
# print (*st)

# N=5
#
# a= [ [1 if i == j else 0 for i in range(N)]  for j in range(N)]
#
# print (a)

#
# print(a := 5, a := a + 1)
#
# d = [1, 2, tr := 3, 6, 3]
#
#
# # while (t := float(input())) > 0: print(t)
#
# # for (t := x) in range(10): print(t)
#
# for (t := x) in range(10): print(t)

#
# s = 0
# while t := float(input()) > 0:
#     s += t
#
# print(s,t)
#
#
#
# lst = [
#     row1 := [1, 2, 3],
#     row2 := [-1, 12, -13],
#     row3 := [7, 8, 2],
# ]
# lst[0], lst[-1] = row3, row1
# # row1, row3 = row3, row1
# print (lst)

# t = (1, 2, 3, 4, 5, 6)

# должен формироваться список:
# #
# # lst = [1, 3, 6, 10, 15, 21]
# s=0
# lst=[s for x in t if (s:=x+s) ]
#
# print(lst)

#
# s = 0
# while   (d := int(input()) ) :
#     if d%2==0:
#         s += d
#     if d==0:
#         break
# print (s)
#

# def f(x):
#     return abs(x) ** 0.5 + 3.2 + x
#
#
# t = tuple(map(float, input().split()))
#
#
# lst=[[y,y**2,y**3] for x in t if (y:=f(x))]
# print (p)
#
#
# m = 1
# while (d := int(input())) >0:
#     if d%3==0:
#         m*=d
# print(m)
# s="Тула Ульяновск Хабаровск Владивосток Омск Уфа"
# l=s.split()
# print (l)
# a=filter(lambda x: len(x)>5,l)
# for i in range(3):
#     print (next(a),end=" ")
#
#
# s="8 11 0 -23 140 1"
#
# # l=list(map(int,s.split()))
# f=list(filter(lambda x : 9<abs(x)<100,map(int,input().split())))
# print (*f)



a="1 5 2 7 10 25 50 100"
b="5 2 3 7 10 25 55"


a=set(a.split())
b=set(b.split())
c=list(filter(lambda x: x%2==0,map(int,a&b)))
print (c)