#0
with open("58322.txt") as f:
    cnt=0
    for s in f:
        m=list(map(int,s.split()))
        m.sort()
        # print (m)
        if m[3]**2>m[0]*m[1]*m[2] or( (m[3]-m[2])==(m[2]-m[1])  and (m[2]-m[1])==(m[1]-m[0])):
            cnt+=1
            print (m,cnt)

