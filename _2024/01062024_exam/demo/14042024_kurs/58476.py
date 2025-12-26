#0
with open("58476.txt") as f:
    cnt=0
    for s in f:
        m=list(map(int,s.split()))

        if len(m)>len(set(m)) and m.count(max(m))==1:
            sr=(sum(m)-max(m))/(len(m)-1)
            # print(sr)
            if max(m)>3*sr:
                cnt+=1
                print(m,cnt)
