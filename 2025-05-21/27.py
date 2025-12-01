from math import *

def cent(clu):
    m=[]
    for p1 in clu:
        suma=0
        for p2 in clu:
            suma+=dist(p1,p2)
        m.append([suma,p1])

    # print (min(m)[1])
    return min(m)[1]

with open("27B_18678.txt") as f:
    s=f.readline()
    # a=[[float(x),float(y)] for x,y in f.strip().split()]
    a=[]
    for s in f:
        a.append(list(map(float,s.strip().replace(',','.').split())))
    clusters=[]
    while a:
        cl=[a.pop()]
        for p1 in cl:
            sosedi=[p2 for p2 in a if dist(p1,p2)<1]

            for p2 in sosedi:
                if p2 in a:
                    a.remove(p2)
                cl.append(p2)
        clusters.append(cl)
    clusters=[x for x in clusters if len(x)>=30]
    print ([len(x) for x in clusters])
px=0
py=0
for c in clusters:
    px+=cent(c)[0]
    py+=cent(c)[1]
px=abs(px*100000/len(clusters)//1)
py=abs(py*100000/len(clusters)//1)
print (px,py)
