from string import *
from itertools import *

s='0123456789AB'
cnt=0
for x in product(s[1:],s,s,s,s):
    # print(x)
    if x.count('7')==1 and x.count('9')+x.count('A')+x.count('B')<=3:
        cnt+=1
        print (x)

print (cnt)
