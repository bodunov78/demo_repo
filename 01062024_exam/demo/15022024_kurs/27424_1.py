f=open("27424.txt")
n=int(f.readline())
ar=[]
for x in f:
    x=list(map(int,x.split()))

    m=[]
    if len(ar)==0:
        ar=[[x[0],x[1]]]
    else:
        for y in ar[-1]:
            m.append(x[0]+y)
            m.append(x[1]+y)
        ar.append(m)

maxa=-10**19
for x in ar[-1]:
    if x%3!=0:
        maxa=max(x,maxa)
print (maxa)