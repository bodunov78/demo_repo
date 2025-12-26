with open("28131_B.txt") as f:
    n=f.readline()
    m=[-1]*120
    print (m)
    maxi=-10**19
    for x in f:
        x=int(x)
        if (x<m[(120-x%120)%120] ) and (x+m[(120-x%120)%120] >maxi):
            maxi=x+m[(120-x%120)%120]
            n=(m[(120-x%120)%120],x)
        if x>m[x%120]:
            m[x%120]=x
    print(maxi,n)
    print (m)