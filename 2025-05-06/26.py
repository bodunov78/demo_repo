with open("26_19256.txt") as f:
    n=int(f.readline())
    a=[x for x in f]

    m=[list(map(int,x.split())) for x in set(a) ]
    m.sort()
    n=set()
    otv=[]
    # print (m)
    j=0
    k=0
    for i in range(0,len(m)-1):

        if m[i][0]==m[i+1][0] and m[i+1][1]-m[i][1]==1:
            n.add(m[i + 1][1])
            n.add(m[i][1])

        else:
            if len(n)>0:
                otv.append([len(n),m[i][0],list(n)])
            n=set()


    otv.sort()
    for x in otv:
        if x[0]==148:
            print (x[0],x[1])
