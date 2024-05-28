with open("63058.txt") as f:
    cnt=0
    for s in f:
        m=list(map(int,s.split()))
        m.sort()
        ms=set(m)
        suma=0
        if len(ms)< len(m) and m.count(m[-1])==1:
            di={x:m.count(x) for x in ms}
            print (di)
            for i,v in di.items():
                if v>1:
                    suma+=i*v
            if suma<m[-1]:
                cnt+=1
    print(cnt)