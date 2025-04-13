from functools import *

# from sys import *
#
# setrecursionlimit(2000)
def ex1():
    print ("X Y Z W")
    for x in (0,1):
        for y in (0, 1):
            for z in (0, 1):
                for w in (0, 1):
                    if ((y <= x) or  (z <= w) or not( z )) == False:
                        print(x,y,z,w)


# результат работы функции
# X Y Z W
# 0 1 1 0



def ex2(s,e):
    if s > e or s==16:
        return 0
    elif s == e:
        return 1
    else:
        return ex2(s + 1, e) + ex2(s * 2, e)

# результат работы
# 84

@lru_cache(None)
def ex3(n):
    if n == 1:
        return 1
    elif n > 1:
        return n*ex3(n-1)

ex1()
# результат работы функции
# X Y Z W
# 0 1 1 0

print (ex2(1,10)*ex2(10,35))
# результат работы
# 84


# заполняем кэш
for x in range(2024):
    ex3(x)
print(ex3(2023)//ex3(2021))
# результат вывода
# 4090506


# print(ex2(1, 10) * ex2(10, 35))

# ex1()
# print (ex2(1,10)*ex2(10,35))