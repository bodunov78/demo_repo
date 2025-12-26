from itertools import *
from pickle import *
from math import *
from functools import *

def dista(p1,p2):
    return (((p1[0]-p2[0])**2 + (p1[1]-p2[1])**2)**0.5)

def fil():
    with open("1002_27_B.txt") as f:
        s=f.readline()
        m=[list(map(float,x.replace(',','.').split()))for x in f ]
        print (m,len(m))
        clusters=[]

        while m:
            cl=[m.pop()]

            print ("cl",cl)

            for x in cl:
                sosedi=[y for y in m if dista(x,y) <2]
                # print ("s",sosedi)
                if len(sosedi)>0:
                    for x in sosedi:
                        if x in m:
                            m.remove(x)

                        cl.append(x)

            clusters.append(cl)


        print([len(x) for x in clusters])

    w=open("27A.dmp","wb")
    dump(clusters,w)
    w.close()

def filr():
    r=open("27A.dmp","rb")
    clusters=load(r)
    print (len(clusters))
    r.close()
    a=[]
    Px=0
    Py=0
    for i,cl in enumerate(clusters):
        a.append([])
        for x in cl:
            suma=0
            for y in cl:
                suma=suma+dista(x,y)
            a[i].append([suma,x])
        a[i].sort()
        print ("ai",i,a[i][:3])
        print ("cent",a[i][0])
        Px+=a[i][0][1][0]
        Py += a[i][0][1][1]

        print (len(cl))
        print (Px*10000/2,Py/2*10000)

        print(abs(Px * 10000 / 2 // 1), abs(Py / 2 * 10000 // 1))


fil()
filr()
