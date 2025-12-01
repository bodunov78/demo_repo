#22:47


from math import *

def centa(clu):

    m=[]
    for p1 in clu:
        suma=0
        for p2 in clu:
            suma+=dist(p1,p2)
        m.append([suma,p1])

    return min(m)[1]


data=[]
with open("27B_18678 (2).txt") as f:
    for s in f:

        s=s.replace(",",".").strip()
        m=list(map(float,s.split()))
        data.append(m)

    print (len(data))
cluster=[]
while data:
    cl=[data.pop()]
    for p1 in cl:
        sosedi=[p2 for p2 in data if dist(p1,p2)<1]
        for x in sosedi:
            if x in data:
                data.remove(x)
            cl.append(x)
    cluster.append(cl)


print ([len(x) for x in cluster ])

px=0
py=0

cluster=[x for x in cluster if len(x) >30]
for cl in cluster:
    px+=centa(cl)[0]
    py += centa(cl)[1]

px=px*100_000/len(cluster)
py=py*100_000/len(cluster)
print (px,py)


# 22:55