s="8"*68
from string import *
L=printable[:36]
print (L)
while '222' in s or '888' in s:
    if '222' in s:
        s=s.replace('222','8',1)
    else:
        s=s.replace('888','2',1)

print (s)

cnt=0
for i in range(100,100000):
    s=str(i)
    for j in range(0,10,2):
        s=s.replace(str(j),'0')

    if s.count('0')==3:
        cnt+=1
print (cnt)

cnt=0
for i in range(100,100000):
    s=str(i)
    s=s.replace('1','').replace('3','').replace('5','').replace('7','').replace('9','')
    if len(s)==3:
        cnt+=1
print (cnt)




s="lksdhjfosdkhjfo834yr038oweihdf09328jhd90j3049u039jhf0394jcj340uif43j093u40fj093u40fj0394ujf039jdfslldkjfoshdkfsdflksdhfkjsd"
suma=0
for i in range(0,36,2):
    suma+=s.count(L[i])
    # s=s.replace(L[i],'0')
    #

print (suma)

n=int(s,36)
cnt=0
while n>0:

    if n%2==0:
        cnt+=1
    n=n//36


print (cnt)
# print (s.count('0'))