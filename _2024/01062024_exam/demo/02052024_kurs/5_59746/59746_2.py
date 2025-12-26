from itertools import *

s='0123456789'
cnt=0
for i in range(2,11):
    for m in permutations(s,i):
        if  m[0]!='0'and ( m[-1]=='0' or m[-1]=='5'):
            cnt+=1

print (cnt+2)