f=open("241.txt")

a=[s for s in f]

maxi=0
for x in a:
    if x.count('A')<25:
        #print(x)
        s=set(x)
        for i in s:
            left=x.index(i)
            right=x.rindex(i)
            maxi=max(maxi,right-left)
            print(left,right,maxi)



