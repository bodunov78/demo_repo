from random import *
d=[3,5,7]
m=[[] for i in range(3) ]
for i,v in enumerate([1023,5017,7001]):
    print (i,v)
    m[i]=[x for x in range(0,100000+1,v)]

print (m)

rndm=[[] for i in range(3)]

for i,v in enumerate([1023,5017,7001]):
    for j in range(20):
        rndm[i].append(m[i][randint(0,len(m[i])-1)])




print (rndm)


# # a=[[] for x in range(100)]
# a=[]
# cnt=0
# for x in range(89,120):
#     if cnt%10==0:
#         a.append([])
#     ind=cnt//10
#     cnt+=1
#     a[ind].append(x)
# print (a)
# b=sum(a,[])
# print (b)
#
# print (randint(0,1000))
#









