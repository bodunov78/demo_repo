from math import *
from itertools import *

def f27A():
    data = []

    def centa(clu):
        a = []
        for p1 in clu:
            suma = 0
            for p2 in clu:
                suma += dist(p1, p2)
            a.append([suma, p1])

        return max(a)[1]

    # with open("demo_2025_22_A.txt") as f:

    with open("27_A_83157.txt") as f:
        for s in f:
            m = list(map(float, s.replace(',', '.').split()))
            # print (m)
            data.append(m)

    clusters = []
    while data:

        cl = [data.pop()]

        for p1 in cl:
            sosedi = [p2 for p2 in data if dist(p1, p2) <1]
            for p2 in sosedi:
                if p2 in data:
                    data.remove(p2)
                cl.append(p2)
        clusters.append(cl)

    # clusters = clusters[3:]

    print([len(cl) for cl in clusters])
    px = 0
    py = 0
    for cl in clusters:
        Q1=0
        Q2=0
        cent=centa(cl)
        print (cent,len(cl),(cent[0]+cent[1])*10_000)

        # for (xy) in cl:
        #     if dist(cent,xy)<=1.2:
        #         Q1+=1
        #     if dist(cent, xy) <= 0.75:
        #         Q2 += 1
        # print (len(cl),Q1,Q2)
        # # k=dist((1.0,0.1),cent)
        print (int(Q1),int(Q2))



    # print (clusters)
    # for cl in clusters:
    #     px += centa(cl)[0]
    #     py += centa(cl)[1]
    #
    # px = px * 10_000 / len(clusters)
    # py = py * 10_000 / len(clusters)

    # print(px // 1, py // 1)

def f27B():
    data = []

    def centa(clu):
        a = []
        for p1 in clu:
            suma = 0
            for p2 in clu:
                suma += dist(p1, p2)
            a.append([suma, p1])

        return max(a)[1]

    # with open("demo_2025_22_A.txt") as f:

    with open("27_B_83157.txt") as f:
        for s in f:
            m = list(map(float, s.replace(',', '.').split()))
            # print (m)
            data.append(m)

    clusters = []
    while data:

        cl = [data.pop()]

        for p1 in cl:
            sosedi = [p2 for p2 in data if dist(p1, p2) < 1]
            for p2 in sosedi:
                if p2 in data:
                    data.remove(p2)
                cl.append(p2)
        clusters.append(cl)

    clusters = clusters[3:]

    print([len(cl) for cl in clusters])
    px = 0
    py = 0
    for cl in clusters:
        Q1=0
        Q2=0
        cent=centa(cl)
        print (int(cent[0]**2+cent[1]**2),int(cent[0]*10_000),int(cent[1]*10_000))
        #
        # for (xy) in cl:
        #     if dist(cent,xy)<=1.2:
        #         Q1+=1
        #     if dist(cent, xy) <= 0.75:
        #         Q2 += 1
        # print (len(cl),Q1,Q2)
        # # k=dist((1.0,0.1),cent)
        # print (int(Q1),int(Q2))



    # print (clusters)
    # for cl in clusters:
    #     px += centa(cl)[0]
    #     py += centa(cl)[1]
    #
    # px = px * 10_000 / len(clusters)
    # py = py * 10_000 / len(clusters)

    # print(px // 1, py // 1)

f27A()
f27B()