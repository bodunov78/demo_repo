from time import *
sleep(2.5)

# 200 300 шаг 1
i=200
while i <= 300:
    print (i)
    i=i+10
#
#
# 300 -200 шаг 5
i=300
while i >= -200:
    print (i)
    i=i-7
    if i <=10:
        break
i=0
while i < 4:
    for x in ("Маша","Наташа","Светлана","Екатерина","Анюта","Люся"):
        print (x)
        if x == "Наташа":
            i=4
            break

    i=i+1
s=10000
flag=0
for i in range(7):
    if flag==1:
        break
    for x in ("Яйца","хлеб", "молоко","Сосиски"):
        # for l in range(10**6):
        #     for m in range(10 ** 2):
        #             True
        s=s-1000
        print (x,s,i)
        if s==5000:
            flag=1
            break



