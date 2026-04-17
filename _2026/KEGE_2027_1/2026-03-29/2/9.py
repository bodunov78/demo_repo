with open ("9.txt") as f:
    for s in f:
        m=list(map(int,s.split()))
        n=[m.count(x) for x in set(m)]
        nm=[(m.count(x),x) for x in set(m)]
        nm.sort()
        n.sort()
        if n==[1,1,1,1,3]:
            print (nm[-1][1])
