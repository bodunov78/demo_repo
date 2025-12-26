#58237

# Сколько существует различных четырёхзначных чисел, записанных в семеричной системе счисления,
# в записи которых цифры следуют слева направо в строго убывающем порядке?
from itertools import *
#product все комбинации из словаря раpмером repeat
# s=("0123456")
# cnt=0
# for x in product(s,repeat=4):
#     # print (x)
#     if int(x[0])>int(x[1])>int(x[2])>int(x[3]):
#         cnt+=1
#         print (x,cnt)



for x in product("AB","12","ZY"):
    print (x)