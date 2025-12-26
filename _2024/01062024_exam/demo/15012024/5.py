s="1?2711*0"
# 10000000000
#   1?2711***0
# 10**10
# ?=(0,1,2,3,4,5,6,7,8,9)
# *=["",0,00,000,1,2,3,4,5..... 999]

x='122'
a=[""]
b=[str(x) for x in range(10)]

for x in range(999):
    a.append(str(x))
    a.append(str(x).zfill(2))
    a.append(str(x).zfill(3))

print(a)
for x in b:
    for y in a:
        st=s.replace('?',x,1).replace("*",y,1)
        if int(st)%4891==0:
            print (st)



# print(x.zfill(3))