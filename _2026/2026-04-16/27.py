from math import *
data = [tuple(map(float, x.replace(",", ".").split())) for x in open("27A_27138.txt")]
cl = []
def c(x): return min((sum(dist(p, k) for p in x), k) for k in x)[1]
while data:
    cl += [[data.pop()]]
    for p in cl[-1]:
        n = [d for d in data if dist(d, p) < 2]
        cl[-1] += n
        for i in n:
            data.remove(i)
a = [x for x in cl if len(x)>10]
cl1 = a[0]
cl2 = a[1]
# cl3 = a[2]
# print (abs(max(cl3)[0])*10000,len(cl1),len(cl2),len(cl3))
m = 0
# for i in cl1:
#     n = sum(dist(i, j) for j in cl2+cl3)
#     if m < n:
#         m = n
#         p = i
# for i in cl2:
#     n = sum(dist(i, j) for j in cl1+cl3)
#     if m < n:
#         m = n
#         p = i
# for i in cl3:
#     n = sum(dist(i, j) for j in cl2+cl1)
#     if m < n:
#         m = n
#         p = i
print(abs(p[0]+p[1])*10000)