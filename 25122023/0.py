a=[]
for i in range(2,66+1):
    a.append(i)
    print (a)

b=[i for i in range(2,66+1)]
print (b)

c=list(range(2,66+1))
print (c)

a=set(range(2,66+1))
b=set(range(30,100+1))
c=set()
c=(a|b)-(a&b)
print (c)
a=list(range(2,66+1))

for i in range(3,10+1):
    if i >3 and i <=10:
        print (a[i])

# for x in a:
#     if x %3 ==0 and x%7 !=0:
#         print (x)

a=[[1,4],[2,3],[7,0],[5,6]]
print (sorted(a))

print( sorted(a, key=lambda x: int(x[1])))

#
#
# for i in range(len(a)):
#     print (a[i])
#
#
#
# for i,v in enumerate(a):
#     if i >4 and v %6 ==0:
#         print (i,v)
#
#
# # c=a[:]
# #
# # for x in a:
# #     if x not in b:
# #         c.add(x)
# # print (c)
# #
# # a=[1,2,3]
# # b=[2,3,4]
# # a+=b
# # print (a)
# #
#
# # for i in range(2,66+1):
# # a={i for i in range(2,66+1)}
# # print (a)
