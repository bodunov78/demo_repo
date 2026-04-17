a=[10,20,10,10,30,40,53,60,70,7777,888]
# for x in a:
#     if x %2==0:
#         print (x)
for i in range(len(a)):
    # if a[i]%2==0:
    print (a[i])
#
for i,v in enumerate(a):
    if v%10==3:
        a[i]=v*(-1)

# a[90]=7779
a.append(99999)
a.insert(100,6666)
# 1 2 3 4 5
# a.remove(10)
# a.remove(10)
# a.remove(10)
# a.remove(10)
# while 10 in a:
#     a.remove(10)

a.pop()
a.pop(0)
# print(a.pop(60))
a.sort(reverse=0)

a=[1,2,3]
b=[3,2,1]
print (id(a),id(b))
a=b.copy()
a=b[::]
print (id(a),id(b))
b.append(7)
print (a,b)
a=0.000000001
print (f"{a:f}")
# a=10
# b=a
# a+=3
# print (a,b)

#
# print (a)