

#3
with open("36040B.txt") as f:
    n=int(f.readline())
    
    mini=[]
    suma=0
    for s in f:
        m=list(map(int,s.split()))
        m.sort()
        # print(m)
        suma+=m[2]
        for i in range(2):
            dd=m[2]-m[i]
            if dd%109!=0:
                mini.append(dd)


    print(suma)
    if suma%109==0:
        print(suma-min(mini))


