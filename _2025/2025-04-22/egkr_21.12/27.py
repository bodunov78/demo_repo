# 21:15
def dist(a,b):
    return ((a[0]-b[0])**2+(a[1]-b[1])**2)**0.5

with open("27B.txt") as f:
    data=[]
    for s in f:
        s=s.replace(',','.')
        m=list(map(float,s.split()))
        data.append(m)
    print(len(data))
    clusters=[]
    # print(data)
    while data:
        cl=[data.pop()]
        print(cl)

        for p in cl:
            sosedi = [x for x in data  if dist(x, p) < 2]

            for x in sosedi:
                cl.append(x)
                if x in data:
                    data.remove(x)

        clusters.append(cl)
    D=[]
    for cl in clusters:
        d=[]
        for a in cl:
            suma=0
            for b in cl:
                suma+=dist(a,b)
            d.append((suma,a))
        D.append(min(d)[-1])
    print (D)
    px=0
    py=0
    for x,y in D:
        px+=x
        py+=y
    px=px/len(D)*10000
    py = py / len(D) * 10000
    print (px,py)