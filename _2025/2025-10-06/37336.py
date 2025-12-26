a=[1,2,3,4,5,6]
for i,x in enumerate(a):
    if x==3:
        a.append(77)
    print (x)


# with open("17 (2).txt") as f:
#     a=[int(x) for x in f]
#     suma=-10**20
#     cnt=0
#     for i in range(0,len(a)):
#         if a[i]%3==0 or a[i+1]%3==0:
#             print (a[i-1],a[i])
#             # if a[i-1]+a[i]>suma:
#             #     suma=a[i-1]+a[i]
#             suma=max(suma,a[i-1]+a[i])
#
#             cnt+=1
#     print (cnt,suma)