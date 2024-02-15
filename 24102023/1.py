# j=0
# for i in (1,4,6,8,0,20,0,0,0,1,1,1,1,1):
#     j+=1
#     print ("Маша-Cаша+Даша=love",j)
# j=0
# for i in range(13):
#     j+=1
#     print ("Маша-Cаша+Даша=love",j)
#

from random import *
from time import *

ts=time()
i=30
while True:
    i=randint(0,100)
    if i%7==0 and i%9==5:
        print ("Счастье есть, оно не может не есть!!!",i)
    if time()-ts > 10:
        break
