di=dict()
m=[]
with open("26_22605_2.txt",encoding="utf-8") as f:
    n=f.readline()
    for s in f:
        x,y,t=list(map(int,s.split()))
        di[(x,y)]=di.get((x,y),[])+[t]
        di[(x,y)].sort()
print (len(di))
for k,v in di.items():
    if len(v)>1:
        for a1,a2 in zip(v,v[1:]):
            m.append((a2-a1,sum(k)))


m.sort()
print (m[:5])
        # print (di[(x,y)])