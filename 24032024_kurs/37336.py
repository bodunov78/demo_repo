#37336

#1

with open("37336.txt") as f:
    a=[int(x) for x in f]
    maxi=-10**19
    cnt=0
    for i in range(len(a)-1):
        if a[i]%3==0 or a[i+1]%3==0:
            maxi=max(maxi,a[i]+a[i+1])
            cnt+=1

    print (cnt,maxi)