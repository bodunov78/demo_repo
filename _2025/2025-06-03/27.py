#23:28
from math import *

data=[]

def centa(clu):
    m=[]

    for p1 in clu:
        suma=0
        for p2 in clu:
            suma+=dist(p1,p2)
        m.append([suma,p1])
    return min(m)[1]




with open("27B_18678 (2).txt") as f:
    for s in f:
        s=s.replace(',','.').strip()
        m=list(map(float,s.split()))
        print (m)
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


m=[len(x) for x in clusters]
clusters=[cl for cl in clusters if len(cl)>30]
print (len(clusters))
px=0
py=0
for cl in clusters:
    px+=centa(cl)[0]
    py += centa(cl)[1]


px=px*1000_000/len(clusters)
py=py*1000_000/len(clusters)

print (px,py)


# 23:36






