#33180
from itertools import *
L="ТИМОФЕЙ"
cnt=0
for x in product(L,repeat=5):
    s="".join(x)
    if s.count('Й')<2 and s[0]!='Й' and s[-1]!='Й' and "ИЙ" not in s and "ЙИ" not in s:
        cnt+=1
print(cnt)










#59831
cnt=0
for x in product("012345678",repeat=5):
    s="".join(x)
    if s[0]=='0':
        continue
    s=s.replace('3','1').replace('7','1')
    # print(s)
    if s.count('5')==1 and s.count('51')==0 and s.count('15')==0:
        cnt+=1
print (cnt)

for i in range(10000,88888+1):
    s=str(i)
    if '9' in s:
        continue
    s = s.replace('3', '1').replace('7', '1')
    # print(s)
    if s.count('5') == 1 and s.count('51') == 0 and s.count('15') == 0:
        cnt += 1
print(cnt)