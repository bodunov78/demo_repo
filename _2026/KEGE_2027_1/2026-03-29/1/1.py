from itertools import *
S="КЁРЛИНГ"
S="кёрлинг"
S=sorted(S)
print ("".join(S))
S="гёиклнр"
# print (ord('А'),ord('Я'),ord('Ё'))
# print (ord('а'),ord('я'),ord('ё'))
cnt=0
for x in product(S,repeat=7):
    cnt+=1
    s="".join(x)
    if s=="кёрлинг":
        print (s,x,cnt)

# cnt=0
# print (S)
# for x in product(S,repeat=3):
#     # print (x)
#     cnt+=1
#     if x.count('В')==1:
#         print(x,cnt)
#     #     cnt+=1
#     #     if "".join(x)=="ЕРН":
    #         print (x,cnt)



