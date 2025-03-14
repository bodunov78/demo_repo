from random import *
a=[1,1,1,1,2,3,4]
cnt=[a.count(x) for x in set(a)]
cnt.sort()
print (cnt,max(cnt))

c=[0,0]
for i in range(1000):
    x=randint(-999,999)

    c[x%2]+=1

print (c)

