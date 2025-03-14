# 38951

#2


with open("38951.txt") as f:
    a=[int(x) for x in f]
    maxi=-10**19
    cnt=0
    for i in range(len(a)-1):
        suma=sum(a[i:i+2])
        if (a[i]%3==0 or a[i+1]%3==0) and suma%5==0:
            maxi=max(maxi,suma)
            cnt+=1
    print(cnt,maxi)