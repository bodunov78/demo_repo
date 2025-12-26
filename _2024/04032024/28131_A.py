with open("28131_B.txt") as f:
    n=f.readline()
    m=[int(x) for x in f]
    print (m)
    # m=[60,140,61,100,300,59]
    maxi=-10**19
    for i in range(len(m)-1):
        for j in range(i+1,len(m)):
            if (m[i]>m[j]) and (m[i]+m[j])%120==0:
                # print ((m[i],m[j]))
                if (m[i]+m[j])>=maxi:
                    maxi=(m[i]+m[j])
                    n=(m[i],m[j])
                    print (len(m),maxi,n)