f = open("27B_57434.txt")
k = int(f.readline())
n = int(f.readline())
maxa = 0
a=[int(x) for x in f ]

# a = [15, 10, 200, 0, 30]
# k = 3
#print(n, len(a))
# for j in range(len(a) - k):
#     for i in range(j + k, len(a)):
#         if a[j] + a[i] >maxa:
#             maxa = a[j] + a[i]
#             print(maxa,a[j],a[i],j,i)



left=a[0]
right=a[k]
suma=left+right
for i in range(k+1,len(a)):
    left=max(left,a[i-k])
    suma=max(suma,left+a[i])
print(suma)

