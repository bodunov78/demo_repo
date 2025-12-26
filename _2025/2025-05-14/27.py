#11:34
from itertools import *
from pickle import *
from math import *
from fnmatch import *


def dista(p1,p2):
    return (((p1[0]-p2[0])**2+(p1[1]-p2[1])**2)**0.5)

def filew():
    with open("27B.txt") as f:

        m=[list(map(float,x.replace(',','.').split())) for x in f]
        print (m)
        clusters=[]
        while m:
            cl=[m.pop()]
            for x in cl:
                sosedi=[ y for y in m if dista(x,y)<2]
                for x in sosedi:
                    if x in m:
                        m.remove(x)
                    cl.append(x)

            clusters.append(cl)

        print (len(clusters))
        a=[]
        for i,cl in enumerate(clusters):
            a.append([])
            for x in cl:
                suma=0
                for y in cl:
                    suma+=dista(x,y)
                a[i].append([suma,x])

            a[i].sort()
        Px=0
        Py=0
        for i in range(len(clusters)):
            Px+=    a[i][0][1][0]
            Py +=   a[i][0][1][1]

        print (Px*10000/len(clusters))
        print(Py * 10000 / len(clusters))


filew()
#11:49