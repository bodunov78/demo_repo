# 4?5*07*3 <=10**9
from time import *
ts=time()

for i in range(0,999999993+1,9341):
    # print (i)
    s=str(i)
    if  '07' in s[3:] and s[0]=='4' and s[-1]=='3' and s[2]=='5'  :
        print (i)

print (time()-ts)
