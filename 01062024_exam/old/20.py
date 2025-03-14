#from adx import *
#from math import *



def f(a,m):
    if a >=sum: return m%2 ==0
     if m==0 : return 0
     h=[f(a+1,m-1),f(a*4,m-1)]
     return any(h) if (m-1)%2 ==0 else all(h)


print ("19:",[s for s in range(1,65) if f(s,2) ])
print ("20:",[s for s in range(1,65) if (not f(s,1)) and f(s,3) ])
print ("21:",[s for s in range(1,65) if (not f(s,2)) and f(s,4) ])







































#def f(a,b,c,m):
#   if a+b<= 20: return c%2 == m%2
#   if c==m: return 0
#   h=[f(a-1,b,c+1,m),f(a,b-1,c+1,m),f(ceil(a/2),b,c+1,m),f(a,ceil(b/2),c+1,m),]
#   return any(h) if (c+1)%2 ==m%2 else any(h)
#for a in range(11,100):
#   for m in range(1,5):
#       if f(a,10,0,m) ==1:
#           print(a,m)
#           break
