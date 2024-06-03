#from itertools import *
#from functools import*
#from adx import *


f=open("26.txt")
n=int(f.readline())
a=[int(x)for x in f]
b=[]
print(len(a),n)
a.sort(reverse=1)
print(a[:10],a[-10:])

i=0
b.append(a[0])
cnt=0
while i < len(a)-1:
    for j in range(i+1,len(a)):
        if a[i]-a[j]>=22:
            b.append(a[j])
            i=j
            print(len(b),a[j])
            break
    
    
    cnt+=1
    if cnt>len(a):
        break
print("OK",len(b),b[-1])
                
