from random import *
a=[1,2,3,4,5,6,7,3,3,3,8,9,3,4,5,4,5,3,2,4,32,3]
for i in range(a.count(3)-2):
    a.remove(3)


# c=2
# pos=len(a)-1
# while True:
#     if pos <0:
#         break
#     if a[pos]==3:
#         if c>0:
#             c-=1
#         else:
#             a.pop(pos)















# a=[randint(0,10) for _ in range(10**3)]
# print (len(a))
# for i in range(a.count(5)-3):
#     a.remove(5)
# print (len(a))


for i in range(len(a)-1,-1,-1):
    if i%2==0 and a[i]==3:
        print (a[i],i)
        a.pop(i)

print (a)

#
# for i,v in enumerate(a):
#     print (i,v)
#     if i%2==0:
#         a.pop(i)


# a=a[::-1]

# n=a.count(3)
# cnt=0
# for i in a:
#     if i