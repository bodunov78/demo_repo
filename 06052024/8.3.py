from itertools import *
from fnmatch import *
suma=10**19
old_sum=4*1
k = [3, 2, 1,0]
a=['000','0010','101','11']


# def fano(a,m):
#     for x in a:
#         for y in m:
#             if fnmatch(y, f"{x}*") or fnmatch(x, f"{y}*"):
#                 m.remove(y)
#
#     print (m)
#     return m
#
# def fano2(m):
#     flag=1
#     for x in m:
#         for y in m:
#              if (fnmatch(y, f"{x}*") or fnmatch(y, f"*{x}")) and x!=y:
#                 return 0
#
#     return 1
#
def fano3(a,m):
    flag=1
    for x in m:
        for y in m:
             if (fnmatch(y, f"{x}*") or fnmatch(y, f"*{x}")) and x!=y:
                return 0

    for x in a:
        for y in m:
             if  fnmatch(y, f"{x}*")    and x!=y:
                return 0

    for x in m:
        for y in a:
             if  fnmatch(y, f"{x}*")  :
                return 0



    return 1


def sums(m):
    global suma
    global k
    for x in permutations(k):
        for y in permutations(m, len(k)):
            if suma > sum([(x[i] * len(y[i])) for i in range(len(k))]):
                # print(x, y)
                suma = sum([(x[i] * len(y[i])) for i in range(len(k))])
                print(suma + old_sum)
                print(x, y)

    # print (m)


m=[]
for x in range(1,5+1):
    for y in product("01",repeat=x):
        s="".join(y)
        m.append(s)

# print(m)

#m=fano(a,m)
#m=fano2(m)
# print ("M",m)



for x in combinations(m,len(k)):
    if fano3(a,x):
        sums(x)
        # print (a,x)





