data = []
with open("1004_27_B.txt") as f :
    s=f.readline()
    for x in f:
        x=x.strip().replace(',','.')
        # print (x)

        data.append(list(map(float,x.split())))


from math import dist

clusters = []
while data:
    cl = [data.pop()]
    for p in cl:
        sosed = [p1 for p1 in data if dist(p,p1)<0.2]
        cl.extend(sosed)
        for p1 in sosed: data.remove(p1)
    clusters.append(cl)

#print([len(cl) for cl in clusters])

from turtle import *
from random import *
tracer(0)
up()
for cl in clusters:
    color = random(), random(), random()
    for x,y in cl:
        goto(x*30, y*30)
        dot(3,color)
update()

def centroid(cl):
    ms, mp = 10**20, [0,0]
    for p in cl:
        s = 0
        for p1 in cl:
            s += dist(p,p1)
        if s < ms:
            ms, mp = s, p
    return mp

cen = [centroid(cl) for cl in clusters]
px = sum(x for x,y in cen)/len(cen)
py = sum(y for x,y in cen)/len(cen)
print(int(px*10000),int(py*10000))