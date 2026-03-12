from itertools import *
ch="02468A"
L="0123456789AB"
cnt=0
for c in product(L,repeat=5):
    s="".join(c)
    for i in ch:
        s=s.replace('3','1').replace('5','1').replace('7','1').replace('9','1').replace('B','1')
        if s.count('1')==2 and s.count(i)==3 and i*3 in s and s[0]!='0':
            cnt+=1
            print (s)
            break

print (cnt)