from math import *
data = [tuple(map(float, x.replace(",", ".").split())) for x in open("27A_2.txt")]
cl = []
def c(x): return min((sum(dist(p, k) for p in x), k) for k in x)[1]
while data:
    cl += [[data.pop()]]
    for p in cl[-1]:
        n = [d for d in data if dist(d, p) < 2]
        cl[-1] += n
        for i in n:
            data.remove(i)
app = [c(x) for x in cl]
print(abs(app[0][0] - app[1][0])*10000, abs(app[0][1] - app[1][1])*10000)