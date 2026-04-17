from itertools import *
a=[10,2,10,4,5]
# for x in permutations([1,2,3,4],3):
#     print (x)
#
# for x in product(a,repeat=2):
#     print (x)
#
# # tipa product
# for x in a:
#     for y in a:
#         for z in a:
#             for w in a:
#                 print (x,y,z,w)

# for x in combinations(a,3):
#     print (x)
#
# for x in a:
#     for y in a:
#         for z in a:
#             if x!=y and x!=z and y!=z:
#                 print (x,y,z)
# kak combinations

for i in range(len(a)):
    for j in range(i+1,len(a)):
        for k in range(j+1,len(a)):
            print (a[i],a[j],a[k])


