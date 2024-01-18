
d=[[3,2,3,3]]
#
while (len(d[0]) !=5):
    X=[]
    for i,a in enumerate(d):
        for x in a:
            b=a[:]
            b.remove(x)
            b=b+[x+1]*2
            b.sort()
            X.append(b)
    d=X

print (d)
Y=set(tuple(x) for x in d )
print (Y)

k=[2]
while max(k) <20:
    for i,v in enumerate(k):
        c=[]
        for x in k:
            c.append(x+1)
            c.append(x *2 )
        print(k,max(k))
    k=c[:]

print(k)