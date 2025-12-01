# 09:06
data=[]
from math import *


def centa(clu):
    a=[]
    for p1 in clu:
        suma=0
        for p2 in clu:
            suma+=dist(p1,p2)
        a.append([suma,p1])

    return min(a)[1]




with open("27_B_17882.txt") as f:
    for s in f:

        m=list(map(float,s.replace(',','.').split()))
        # print (m)
        data.append(m)


clusters=[]
while data:

    cl=[data.pop()]

    for p1 in cl:
        sosedi=[p2 for p2 in data if dist(p1,p2)<1]
        for p2 in sosedi:
            if p2 in data:
                data.remove(p2)
            cl.append(p2)
    clusters.append(cl)

print ([len(cl) for cl in clusters])

px=0
py=0

for cl in clusters:
    px+=centa(cl)[0]
    py += centa(cl)[1]

px=px*10_000/len(clusters)
py=py*10_000/len(clusters)

print (px//1,py//1)
