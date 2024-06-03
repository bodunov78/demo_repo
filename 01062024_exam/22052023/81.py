from itertools import *
s="БКФЦ"
i=0

a=product(s,repeat=5)
for x in a:
   i+=1
   print(i,x)
   if i==486:
      break


