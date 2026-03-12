s="8"*68
while '222' in s or '888' in s:
    if '222' in s:
        s=s.replace('222','8',1)
    else:
        s=s.replace('888','2',1)

print (s)
cnt=0
for i in range(1234,23433,3):
    s=str(i)
    # s=s.replace('2','0').replace('4','0').replace('6','0').replace('8','0')
    # s = s.replace('1', '').replace('3', '').replace('5', '').replace('7', '').replace('9','')
    print (s)
    suma=0
    for i in range(0,10,2):
        suma=suma+s.count(i)
    if suma==3:
        cnt+=1

    if s.count('0')+s.count('2')+s.count('4')+s.count('6')+s.count('8')==3:
        cnt+=1
    # if len(s)==3:
    #     cnt+=1
    print (cnt)
#     if s.count('0')==3:
#         cnt+=1
#         print(s)
# print (cnt)