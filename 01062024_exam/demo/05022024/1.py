from itertools import *
c=(1,4,5)

a=[[] for x in range(69) ]
print (a)


for x in range(0,69):
    a[x].append([x])
    for j in range(1,5):
        a[x].append([])
        for m in a[x][j-1]:
            # a[x][j].append(m + 1)
            # a[x][j].append(m + 4)
            # a[x][j].append(m * 5)
            # a[x][j].append((m * 5, m+4, m+1))
            # maxi=max(m+1,m+4,m*5)
            if j==2 or j==4:
                a[x][j].append(min(m+1,m+4,m*5))
            else:
                a[x][j].append(max(m + 1, m + 4, m * 5))

            # print(x,m,m+1,m+4,m*5,a[x])
            # a[x][j].append(maxi)

            # a[x][j].append(max(m +1,m+4,m*5))
        # a[x][j].sort()
for x in range(1,69):
    print(a[x])

#
#
#
# for k in range(67):
#
#     a=[]
#     for x in product(c, repeat=3):
#         s=k
#         for i,y in enumerate( x):
#             if y==1:
#                 s+=1
#                 arr[k][i].append(s)
#             elif y == 4:
#                 s += 4
#                 arr[k][i].append(s)
#             elif y == 5:
#                 s =s* 5
#                 arr[k][i].append(s)
#         if s>=68:
#             print("s:",s)
#             a.append(f"{str(x)}:{str(k)}")
#     print(a)
#
# print (arr[0])
