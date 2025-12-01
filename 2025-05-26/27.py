# 0:49
from math import *
cluster=[]
data=[]

def cent(clu):

    m=[]
    for p1 in clu:
        suma=0
        for p2 in clu:
            suma+=dist(p1,p2)
        m.append([suma,p1])
    # print (min(m)[1])
    return min(m)[1]

with open("27_B_21425.txt") as f:
    for s in f:
        s=s.strip().replace(',','.')
        m=list(map(float,s.split()))
        # m=[float(x) for x in s]
        data.append(m)
    # print (len(data))
    while data:
        cl=[data.pop()]
        for p1 in cl:
            sosedi=[p2 for p2 in data if dist(p1,p2)<4]
            for p2 in sosedi:
                if p2 in data:
                    data.remove(p2)
                cl.append(p2)
        cluster.append(cl)

    print ([len(x) for x in cluster])
    px=0
    py=0
    for x in cluster:
        px+=cent(x)[0]
        py+=cent(x)[1]
    px=px*10000/len(cluster)
    py = py * 10000 // len(cluster)

    print(px,py)
