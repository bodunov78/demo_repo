from random import *
arr=[randint(1,100) for i in range(10**6)]

# arr=[2,3,5,4,66,77,88,56,65,33,33333,0,-10]

N=int(input("На что делим?:"))
deli=[0]*N
print (deli)

for i,v in enumerate(arr):
    deli[v%N]+=1

print(deli,deli.__sizeof__())
