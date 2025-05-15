#1:23

with open("17_19249.txt") as f:
    a=[x for x in f]
    # print (len(a))
    m=[]
    n=[]
    z=[]
    cnt=0
    for x in a:
        x=x.strip()
        # print (x)
        if (len(x) == 5 and x[-2:] == '43'):
            n.append(int(x))

            print(n[-1])
    maxi=max(n)

    for a1,a2,a3 in zip(a,a[1:],a[2:]):
        m = []
        print(a1,a2,a3)
        if (10000<=abs(int(a1))<100000 and a1[-2:]=='43') or (10000<=abs(int(a2))<100000 and a2[-2:]=='43') or (10000<=abs(int(a1))<100000 and a3[-2:]=='43'):

            j=int(a1)**2+int(a2)**2+int(a3)**2
            print(j)
            if j <= maxi**2:
                cnt+=1
                z.append(j)


    print (cnt,type(z))

