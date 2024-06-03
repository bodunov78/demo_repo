with open("27423.txt") as f:
    n,m=map(int,f.readline().split())
    print (n,m)
    a=[int(x) for x in f]
    a.sort()
    print (len(a),a[0])
    for i in range(1,len(a)):
        if sum(a[:i])<=n:
            # print (sum(a[:i]))
            suma=sum(a[:i-1])
            print (suma)
            sumi=i
    for j in range(sumi,len(a)):
        if suma+a[j] <=n:
            print (suma+a[j],a[j])