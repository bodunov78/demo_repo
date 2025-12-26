def che(n):
    s = str(abs(n))
    if len(s) == 4 and s.count('3') == 2:
        return 1
    else:
        return 0


with open("1004_17.txt") as f:

    m=[int(x) for x in f]
    print (len(m))

    maxf=-10**19
    for x in m:
        if che(x):
            maxf=max(maxf,x)

    print(maxf)
    cnt=0
    maxs=-10**10
    for a1,a2,a3 in zip(m,m[1:],m[2:]):
        if che(a1)+che(a2)+che(a3)<=2 and a1+a2+a3<=maxf:
            print (a1,a2,a3)
            cnt+=1
            maxs=max(maxs,a1+a2+a3)

    print (cnt,maxs)