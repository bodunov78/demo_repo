with open("35913.txt") as f:
    nmin=10**19
    for s in f:
        s=s.strip()
        us=list(set(s))
        us.sort()

        n=s.count('N')
        if n<nmin:
            nmin=min(n,nmin)
            umax=-10**19
            for x in us:
                sx=s.count(x)
                if sx >= umax:
                    umax=max(umax,sx)

                    print(n,nmin, us,x,umax , s)
