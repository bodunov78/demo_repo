# 4?82*1*7 <=10**9
from time import *
ts=time()
for i in range(0,499999997+1,9111):
    s=str(i)
    if  s[-1]=='7'and  s[2:4]=='82' and '1' in s[4:]  and s[0]=='4':
        print (i)
print (time()-ts)