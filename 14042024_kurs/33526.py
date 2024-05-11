#2
with open("33526.txt") as f:
    i=0
    s=f.readline().strip()
    us=list(set(s))
    di={x:0 for x in set(s)}
    print(di)
    for i in range(len(s)-2):
        if s[i]==s[i+2]:
            di[s[i+1]]+=1
    print(di)
    maxi=-10**19
    for x,y in di.items():
        if y > maxi:
            maxi=y
            print(x,maxi)


