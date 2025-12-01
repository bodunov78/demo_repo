with open("9.txt") as f:
    c=[]
    for s in f:
        s=s.strip()
        a=[int(x) for x in s.split()]
        a=list(map(int,s.split()))
        a.sort(reverse=1)
        c.append(set(a))
        if len(a)==len(set(a))
        print (a)

    print(len(c),c[:20])