from itertools import *
a=[0,1,2,3]
    [0,1,2]
    0,1,3
    0, 2 , 3
    1,2,3

    2,3,1
    3,1,2
    2,1,3
    1,3,2
    3,2,1


# аналог product(a,repeat=4)
# for x in a:
#     for y in a:
#         for z in a:
#             for w in a:
#                 if x!=y and x!=z and x!=w and y!=z and y!=w and z!=w:
#                     print (x,y,z,w)
#
# for x in product(a,repeat=4):
#     print (*x)

for i0 in range(len(a)):
    for i1 in range(i0+1,len(a)):
        for i2 in range(i1+1,len(a)):
            for i3 in range(i2+1,len(a)):
                print (a[i0],a[i1],a[i2],a[i3])

for x in combinations(a,4):
    print (*x)

for x in permutations(a,4):
    print (x)



for x in range(10):
    if x%3 !=0:
        a.append(x**2+3)

print (a)

a=[ x**2+3 for x in range(10) if x%3 !=0]
print (a)