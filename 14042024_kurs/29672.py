with open("29672.txt") as f:
    s=f.readline().strip()
    m=[-1]
    k=set(s)
    print(k)
    for i,v in enumerate(s):
        if v=='Y':
            m.append(i)

m.append(len(s))
n=100+1
maxi=-10**19
for i in range(0,len(m)-n):
    maxi=max(maxi,m[i+n]-m[i]-1)
    # print (maxi)

print(maxi)

n=3+1
a=[-1,3,5,9,20,50,100,150,200]
for i in range(len(a)-n):
    print(i,a[i+n]-a[i]-1)