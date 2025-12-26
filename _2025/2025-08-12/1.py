# import sys
#
# # считывание списка из входного потока
# # lst_in = list(map(str.strip, sys.stdin.readlines()))
#
# # здесь продолжайте программу (используйте список lst_in)
# lst_in=["зонт=1000","палатка=10000","спички=22","котелок=543"]
#
# # a=tuple(map(str,x.split('=')) for x in lst_in)
# # print (lst_in)
# # print (a)
#
#
# # a=tuple((tuple(x.split("="))) for x in lst_in)
# a=tuple((tuple(x.split("="))) for x in lst_in)
#
# # b=tuple(filter(lamda x,y: int(y)<500 , s.split('=') ) for s in lst_in))
#
# f = filter(lambda x: int(x[1]) >= 500, a)
# gen = map(lambda x: x[0], f)
# print(*gen)
# from string import *
#
# def prov(s):
#     shab=set(printable[:36]+'@'+'.'+'_')
#     # print (shab)
#     if set(s)==shab&set(s) and '@' in s and '.' in s.split('@')[1]:
#         return 1
#     else:
#         return 0
#
#
#
# s="abc@it.ru dfd3.ru@mail biba123@list.ru sc_lib@list.ru $fg9@fd.com"
#
# a=filter(prov,s.split())
# print (*a)

# a="-7 8 11 -1 3"
# b="1 2 3 4 5 6 7 8 9 10"
# a=list(map(int,a.split()))
# b=list(map(int,b.split()))
#
# c=list(zip(a,b))
#
# print (*list(c[i][0]*c[i][1] for i in range(3)  ))

#
# lst_in = ['1 2 3 4', '5 6 7 8', '7 8 9 0', '9 0 1 2']
# a=[tuple(map(int,x.split())) for x in lst_in ]
#
# # print (a)
# # m=list(zip(*zip(*a)))
# m=list(zip(*lst_in))
# print (*m)
# # m=list(*zip(*a))
# #
# for x in m:
#     print (*x,end="")
# # # # print (m)
# # # m=*zip(*zip(*a))
# # # for x in m:
# # #     print (x)
# # print (*zip(*zip(*a)),end='\n')


s="Москва Уфа Тула Самара Омск Воронеж Владивосток Лондон Калининград Севастополь"
a=list(s.split())
st = iter(a)
for x in zip(st, st, st):
    print(*x)