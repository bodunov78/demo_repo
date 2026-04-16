with open("13.txt") as f:
    m=list(map(int,f.readlines()))
    print (m)
    k=[x for x in m if x%15!=0]
    N=min(k)
    cnt=0
    maxsum=-10**20
    for a1,a2 in zip(m,m[1:]):
        if a1%N==0 and a2%N==0:
            suma=a1+a2
            cnt+=1
            maxsum=max(maxsum,suma)
    print(cnt,maxsum)
