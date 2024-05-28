from time import *
ts=time()
cnt=0
for i in range(0,10**10,5):
    if i%100000000==0:
        print (i,time()-ts)
    if len(str(i))==len(set(str(i))):
        cnt+=1

print (cnt,time()-ts)
