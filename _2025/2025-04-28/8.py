#0:32

from itertools import *

s=sorted("ЯНВАРЬ")
print (s)
cnt=0
for x in product(s,repeat=5):
    cnt+=1
    x="".join(x)
    if x[0]!='Я' and x.count('Ь')<2 and 'ЯЯ' not in x:
        print (x,cnt)

#0:36
