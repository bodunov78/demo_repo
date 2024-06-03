
# a=("К":"001","Н":"100","Р":111","М":"","Л":"","":""
# "К", "Л", "М", "Н", "О", "П", "Р", "С"
Z=set()
from itertools import *
from fnmatch import *
def clr(a,b):
    d=[]
    for x in b:
        for y in a:
            k = f"{y}*"
            m = f"{x}*"
            if fnmatch(x, k):
                d.append(y)
            if fnmatch(y, m):
                d.append(y)

    #print("set d",set(d))
    a = list(set(a))
    d = list(set(d))

    #print("set a", a)
    #print("a", a)

    a.sort()
    for x in set(d):
        a.remove(x)

    return a

def cmb(a,b,n):


    #print("A-N",a,n)
    #print("B-N", a, n)


    if len(a)==0 or len(b)==8:

        # print("B=",b)
        # b.sort()
        k=[len(x) for x in b[3:]]


        k.sort()

        #print("B=",k)
        Z.add(tuple(k))

    else:
        n+=1
        for x in a:

            na=a[:]
            nb=b[:]
            nb.append(x)
            # print("na",na)
            # print("nb", nb)

            na=clr(na,nb)
            cmb(na,nb,n)





a=[bin(x)[2:].zfill(y) for x in range(20) for y in range(1,5)]
print (a)
b=["001","100","111"]
v=[1,4,8]
d=[1,1,2,4,0]




a=list(clr(a,b))
cmb(a,b,0)

for v in Z:
    if len(v)==5:
        for x  in permutations(v):
            print(x,d,sum([x[i]*d[i] for i in range(len(x))]))

print(Z)


#print(a)
#print(b)