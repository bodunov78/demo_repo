#64947

#6
with open("64947.txt") as f:
    a=[int(x) for x in f]
    k832=max(x for x in a if x%1000==832)

    k832=-10**19
    for x in a:
        if x%1000==832:
            k832=max(k832,x)





    cnt=0
    maxi=-10**19
    for i in range(len(a)-2):
        m=a[i:i+3]
        # print (a[-1],m)

        k3=0
        k5=0
        k4=0
        for i in m:
            if 1000<=i<9999:
                k4+=1
            if i%3==0:
                k3+=1
            if i%5==0:
                k5+=1

        if 1<=k4<3 and k5>k3 and sum(m)>k832:
            # print (m)
            maxi=max(maxi,sum(m))
            cnt+=1

    print(cnt,maxi)