with open("17 (4).txt") as f:
    m=[int(x) for x in f]
    mn=[x for x in m if str(x)[-1]==str(x)[-2]]
    print (min(mn))
    cnt=0
    maxs=-1
    for a1,a2 in zip(m,m[1:]):
        if ((a1%7==0)^(a2%7==0)):
            if (str(a1)[-1]==str(a2)[-2]) or (str(a2)[-1]==str(a1)[-2]):
                if a1**2+a2**2 <=(min(mn)**2):
                    cnt+=1
                    maxs=max(maxs,a1**2+a2**2)
                    print (a1,a2)
    print (cnt,maxs)