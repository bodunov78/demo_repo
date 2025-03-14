from random import *
arr=[randint(1,100) for i in range(10**6)]


N=int(input("На что делим?:"))
deli=dict()

for i in range(N):
    deli[i]=0
print(deli)

for i in arr:
    deli[i%N]+=1

print(deli,deli.__sizeof__())
