with open("27989_A.txt") as f:
    n=f.readline()
    cnt=0
    a=[int(x) for x in f ]
    # a=[2,6,13,39]
    for i in range(len(a)-1):
        for j in range(i+1,len(a)):
            if a[i]*a[j]%26==0:
                cnt+=1
    print (cnt)