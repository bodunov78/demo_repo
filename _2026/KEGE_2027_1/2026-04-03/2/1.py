d=dict()
x=123
i=10
d[x]=d.get(x,[])+[i]
i=20
d[x]=d.get(x,[])+[i]

print (d[x])