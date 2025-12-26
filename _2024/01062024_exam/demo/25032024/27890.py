#2

with open("27890A.txt") as f:
    n=int(f.readline())
    dd=[]
    suma=0
    for s in f:
        m=list(map(int,s.split()))
        suma+=max(m)
        if (max(m)-min(m))%5!=0:
            dd.append(max(m)-min(m))

    print(suma)
    if suma%5==0:
        suma=suma-min(dd)
    print(suma)