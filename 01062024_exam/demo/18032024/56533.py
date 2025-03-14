from time import *
ts=time()
s=bin(987654321//8)[2:]
e=bin(2123456789//8)[2:]
print (s,e)
print(987654321//8)
print (2123456789//8)
m=[]


for x in range((987654321//8)-10,(987654321//8)+10):
    y=x
    for i in range(3):
        if sum(list(map(int,list(str(x)))))%2==1:
            y=y*2+1
        else:
            y = y * 2
    if  987654321<=y<=2123456789:
        m.append(x)

    for x in range((2123456789 // 8) - 10, (2123456789 // 8) + 10):
        y = x
        for i in range(3):
            if sum(list(map(int, list(str(x))))) % 2 == 1:
                y = y * 2 + 1
            else:
                y = y * 2
        if 987654321 <= y <= 2123456789:
            m.append(x)

    # print (x)
cnt=0
for i in range(min(m),max(m)+1):
    cnt+=1

print (cnt)
print(time()-ts)