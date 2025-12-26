#a=input("Введите число")
#print (a)
#b=int(input("Введи целое число"))
#c=float(input("Введи вещественное число"))
from time import *
ts=time()
a=0
b=100
#print (type(a),type(b),type(c),c,int(c))
while a<10:
    print (a,b)
    a=a-1
    b=100
    while b<1000000:
        if time()-ts> 5:
            break
        b+=1



