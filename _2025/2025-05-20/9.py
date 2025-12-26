with open("9.txt") as f:
    n=[ list(map(int,x.split())) for x in f]
    print (n)
    cnt=0
    for m in n:

        a=[m.count(s) for s in set(m)]
        a.sort()
        if a==[1,1,2,3]:
            # print (a,m)
            p = [int(x) for x in m if m.count(x) > 1]
            n = [int(x) for x in m if m.count(x) == 1]
            if (sum(n) / len(n)) > sum(p) / len(p):
                    # count += 1
                    print(p,n)
                    cnt+=1
    print (cnt)