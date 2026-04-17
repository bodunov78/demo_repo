with open("55596.txt") as f:
    i=0
    d=dict()
    m=[]
    for s in f:
        a=list(map(int,s.split()))
        m.append(a)
        for x in a:
            d[x]=d.get(x,[])+[i]
        i+=1

cnt=0
for a in m:

    for x in a:
        if a.count(x)==1 and len(d[x])==46:
            print (a,x,len(d[x]))
            cnt+=1
            break

print (cnt)

