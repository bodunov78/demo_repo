with open("9.txt") as f:
    a=[]
    for s in f:
        s=s.strip()
        # m=list(map(int,s.split()))
        m=[int(x) for x in s.split()]
        a.append(m)
        # print (m

print (len(a))


for m in a:
    mid=(sum(m)/len(m)//1)
    if mid in m:
        print (m)
