from itertools import *


cnt=0
print ("йохохо")
for x in product(sorted("ВЕРОНИКА"),repeat=3):
    if x.count('В')==1:
        cnt+=1
        if x.count('А')==0:
           print (x,cnt)
           break
