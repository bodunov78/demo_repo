from itertools import *
k=(0,1,2,3,4,5,6,7,8,9)
a=[x for x in product(k,repeat=1) ]
print (a)

 # from fnmatch import *
cnt=0
for x in range (10):
    for y in range(0,100):
        s=f"1{x}2711{y}0"
        if int(s)%4891==0:
            cnt+=1
            print (s,cnt)

for y in range(0,1000):
     s=f"12711{y}0"
     if int(s)%4891==0:
        cnt+=1
        print (s,cnt)

