#39763
with open("17.txt") as f:
    maxi_sum=-10**19
    cnt=0
    a=[int(x) for x in f]
    print (len(a))
    for i in range(len(a)-2):
        m=a[i:i+3]
        m.sort()
        if m[2]**2<m[0]**2+m[1]**2:
            maxi_sum=max(sum(m),maxi_sum)
            cnt+=1
    print (cnt,maxi_sum)