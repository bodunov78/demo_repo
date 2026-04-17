from itertools import *
# cnt=0
# for a in product((1,2,3,4),repeat=3):
#     cnt+=1
#     print (a,cnt)
#
# cnt=0
# for x in product((1,2,3),(4,5,6),(0,1)):
#     cnt+=1
#     print (x,cnt)

# for x in permutations((1,2,3,4,5),3):
#     print (x)
#
for a1,a2,a3 in product((1,2,3,4,5),repeat=3):
    if a1+a3>a2:
        print (a3,a2,a1)

for a in product((1,2,3,4,5),repeat=3):
    if a[0]+a[2]>a[1]:
        print (a)
cnt=0
for i in range(100,999+1):
    ed=i%10
    des=i//10%10
    sot=i//100
    if ed+sot>des and ( ed < 4 and sot < 4 and des <4):
        cnt+=1
        print (i,cnt)