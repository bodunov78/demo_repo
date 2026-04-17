with open("17 (5).txt") as f:
    a=[]
    b=[]
    for s in f:
        a.append(int(s))
    for a1,a2 in zip(a,a[1:]):
        if (a1*a2)%3==0:
            b.append((a1+a2,a1,a2))

print (max(b))