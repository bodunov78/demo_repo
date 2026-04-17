from time import *
ts=time()
cnt=0
for i in range(20,300+1):
    for j in range(50,6000+1):
        cnt+=1
        if cnt%18000==0:
            print ((i,j),cnt)
print (cnt)
print (time() -ts)
 a,b,c [1,100]
 a^2+b^2=c^2