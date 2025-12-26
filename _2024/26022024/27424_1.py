with open("27424_A.txt") as f:
    n=int(f.readline())
    a=[]
    maxi=-10**19
    for i in range(n):
        x, y =f.readline().split()
        x=int(x)
        y=int(y)
        if len(a)>0:
            m=[]
            for z in a[-1]:
                m.append(z+x)
                m.append(z + y)
            a.append(m)
        else:
            a.append([x,y])
    for x in a[-1]:
            if x%3!=0:
                maxi=max(maxi,x)
                print (maxi)
    print (len(a[-1]))