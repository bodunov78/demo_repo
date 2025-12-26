with open("35916B.txt") as f:
    a=[[] for i in range(3)]
    for x in f:
        x=int(x)
        a[x%3].append(x)
    for i in range(3):
        a[i].sort()
    c=min([sum(a[i][:3]) for i in range(3)])
    d=sum(a[i][0] for i in range(3))
    print(c,d)