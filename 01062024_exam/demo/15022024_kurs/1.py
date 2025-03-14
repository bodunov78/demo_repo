f=open("27424.txt")
n=int(f.readline())
m=[]
maxa=-10**19
for x in f:
    s=list(map(int,x.split()))
    print (s)
    m1=[]
    if len(m)>0 :

        for j in m:
            m1.append(j+s[0])
            m1.append(j + s[1])
    else:
        m1.append(s[0])
        m1.append(s[1])
    m=m1[:]

for x in m:
    if x%3 !=0:
        maxa=max(maxa,x)
        # print (maxa)

print (maxa)