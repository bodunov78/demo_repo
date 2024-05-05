from itertools import *
from fnmatch import *
suma=10**19
old_sum=0
k = [3, 2,1,0]
a=['010','1101','011','10']
#
def fano3(a,m):
    flag=1
    for x in m:
        for y in m:

             if (fnmatch(y, f"{x}*")) and x != y:
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
            if suma >= sum([(x[i] * len(y[i])) for i in range(len(k))]):
                # print(x, y)
                suma = sum([(x[i] * len(y[i])) for i in range(len(k))])
                print(suma + old_sum)
                print(x, y)

    # print (m)


m=[]
for x in range(1,6+1):
    for y in product("01",repeat=x):
        s="".join(y)
        m.append(s)



for x in combinations(m,len(k)):
    if fano3(a,x):
        sums(x)
        # print (a,x)





