from random import *
# a=[[] for x in range(100)]
a=[]
cnt=0
for x in range(89,120):
    if cnt%10==0:
        a.append([])
    ind=cnt//10
    cnt+=1
    a[ind].append(x)
print (a)
b=sum(a,[])
print (b)

print (randint(0,1000))










