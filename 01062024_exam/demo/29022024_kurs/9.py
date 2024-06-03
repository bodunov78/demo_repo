#63058

with open("9.txt") as f:
    # a=[list(map(int,x.split())) for x in f]
    cnt=0
    for s in f:
        a=list(map(int,s.split()))
        a.sort()
        b=set(a)

        if len(b)<len(a) and a.count(max(a))==1:
            suma=0
            for x in b:
                if a.count(x)>1:
                    suma+=x*(a.count(x))
            if suma<max(a):
                cnt+=1
    print (cnt)