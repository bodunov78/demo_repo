
with open("45260.txt") as f:
    n=int(f.readline())
    a=[]
    maxi=-10**19
    for s in f:
         s=list(map(int,s.split()))
         a.append(s)
    a.sort()
    print (a)

    b=[[] for i in range(100000)]
    for i in range(len(a)):
        b[a[i][0]].append(a[i][1])
    print (b)

    for j,x in enumerate( b):
        if len(x)>2:
            for i in range(1,len(x)):
                m=x[i]-x[i-1]-1
                if m==13:
                    print (j,x[i-1],x[i])

    # for i in range(len(a)-1):
    #     for j in (i+1,len(a)):
    #         if a[i][0]==a[j][0]:
    #             d.add(a[i][1])
    #             d.add(a[j][1])
    #         else:
    #             print (d)
    #             d={}
