from itertools import *

print ("".join(sorted("кёрлинг")))
L="гёиклнр"
for i,v in enumerate(product(L,repeat=5),1):
    print (v,i)
cnt=0
for x in L:
    cnt+=1
    print (x,cnt)

for i,v in enumerate(L,1):
    print (v,i)




# print (ord('а'),ord('я'))
# print (ord('А'),ord('Я'))
# print (ord('ё'),ord('Ё'))
#
# for i in range(1040,1071+1):
#     print (i,chr(i))
#
# print (chr(1104))
#

