from math import *
from time import *
from random import *
def simp(n):
    print (n)
    ts=time()
    a=[2,3,5,7,11,13,17,19,23]
    for i in range(23,ceil(n**0.5)+2,2):
    # for i in range(23, n + 2, 2):

        flag=0
        for c in a:
            if i%c==0:
                flag=1
                break
        if flag==0:
            a.append(i)
    # print (a)
    print (time()-ts)
    return a


# print (len(simp(10_010_300_000)))
def fn(n):
    a=simp(n)
    k=n
    print (a)
    d=[]
    while n>1:
        for i in a:
            print ("i",i,n)
            while n%i==0:
                d.append(i)
                d.append(n//i)
                n=n//i
                # print (i,n)
        else:
            d.append(n)
            break
    print (k,d)
    return (d)
n=randint(110_250_000, 110_300_000)
fn(n)