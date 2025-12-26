from time import *
ts=time()
with open("24-263.txt") as f:
    s=f.readline()
    m=10_000
    for l in range(len(s)):
        for r in range(l+m,l,-1):
            ss=s[l:r+1]
            if ss.count('C') >=120:
                m=min(m,len(ss))
            else:
                break

    a=[]
    for i,v in enumerate(s):
        if v=='C':
            a.append(i)

print (len(a))
for i in range(10,len(s)):
    print ((a[i-10:i]))


print (m,time()-ts)

