from random import *
a=set()
b=[]


print ()
for i in range(10):
    # a.add(randint(1,100))
    b.append(randint(1,5))

print (b,set(b))


c=[]
# for i in range(10):
#     x=randint(1,5)
#     print (x)
#     if x not in c:
#         c.append(x)
#
# print (c)



i=randint(0,99)
while i  in a:
    i = randint(0, 99)


while len(c)<=10:
    x = randint(1, 15)
    print(x)
    if x not in c:
        c.append(x)



print (c)



a=[0]*13
print (a)
for i in range(13):
    a[i]=randint(0,5)

print (set(a))