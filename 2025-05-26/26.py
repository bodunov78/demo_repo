with open("26_21424.txt") as f:
    n=f.readline()
    m=[int(x) for x in f]
    print (len(m))
    m.sort(reverse=1)
    a=[1]*len(m)
    for i in range(len(m)):
        for j in range(i):
            if m[j]-m[i]>=9:
                a[i]=max(a[i],a[j]+1)

    # print(max(a))
    for i in range(len(m)):
        if a[i]==1040:
            print (m[i])