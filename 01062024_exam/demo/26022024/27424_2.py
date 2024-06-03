with open("27424_B.txt") as f:
    n=int(f.readline())
    dmin=10**19
    suma=0
    for x in f:
        a=list(map(int,x.split()))
        suma+=max(a)
        if (max(a)-min(a))%3!=0:
            dmin=min(dmin,max(a)-min(a))

    if suma%3==0:
        suma=suma-dmin
    print (suma)