from itertools import *

s="01234"

#Возвращает подпоследовательности длины r из элементов итерируемого объекта, подаваемого на вход.
for x in combinations(s,3):
    print (x)


#Возвращает последовательные r перестановок элементов в итерируемом объекте
# for x in permutations(s,3):
#     print (x)

#Декартово произведение итерируемых объектов, подаваемых на вход.

# for x in product(s,repeat=2):
#     print (x)

# a=[]
# for x in product(s,repeat=3):
#     a.append("".join(x))
# print (a)

# a=[[1,2,3,4],[5,6,7,8],[9,0,1,2],[3,4,5,6]]
# print (a)
# b=list(zip(*a))
#
# for i in a:
#     print (*i)
#
# print (b)
# for i in b:
#     print (*i)