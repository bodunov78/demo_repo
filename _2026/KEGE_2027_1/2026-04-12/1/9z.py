from math import *
# количество символов
L=1310
i=ceil(log2(L))
n=270
K=ceil(n*i/8)
disk=290*1024
user=disk//K
print (i,K,user)