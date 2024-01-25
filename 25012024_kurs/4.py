from random import *
a=[[] for i in range(3)]
cnt=0
m1023=[x for x in range(0,100000,1023)]
print (len(m1023),m1023)
print (m1023[randint(0,97)])




for i,v in enumerate([1023,5017,7001]):
    while len(a[i])<20:
        cnt+=1
        x=randint(0,100000)
        if x%v==0:
            a[i].append(x)

print (cnt,a)













