from itertools import *
#
# for s in product("ABCD",repeat=4):
#     print (s)
#
# for c1 in "ABCD":
#     for c2 in "ABCD":
#         for c3 in "ABCD":
#             for c4 in "ABCD":
#                 print ((c1,c2,c3,c4))

for x in combinations("ABCD",2):
    print (x)
s="ABCD"
for i in range(len(s)):
    for j in range(i+1,len(s)):
        for k in range(j+1,len(s)):
            print ((s[i],s[j],s[k]))

for i in range(len(s)):
    for j in range(len(s)):
        for k in range(len(s)):
            if i< j <k :
                print ((s[i],s[j],s[k]))

for x in permutations(s,4):
    print (x)

s=[1,2,3,4,5]
#
for x in s:
    s1=s[:]
    s1.remove(x)
    for y in s1:
        s2=s1[:]
        s2.remove(y)
        for z in s2:
            s3=s2[:]
            s3.remove(z)
            for q in s3:
                s4=s3[:]
                s4.remove(q)
                for w in s4:
                    print (x,y,z,q,w)
#

# a=5
# b=10
# print(id(a),id(b))
# c=a
# print(id(a),id(b),id(c))
# a=b
# b=c
# c+=222
# print(id(a),id(b),id(c))
#
# a=[1,2,3,4,5]
# b=[9,8,7,6,5]
# c=a[::]
# c=a.copy()
# print (id(a),id(b),id(c))
# c.append(999)
# a.append(777)
# print (id(a),id(b),id(c))
