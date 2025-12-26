from time import *
ts=time()
with open("24_17535.txt") as f:
    s=f.readline()
    print(len(s))
    m=100_000
    for l in range(len(s)):
        for r in range(l+m,len(s)):
            ss=s[l:r+1]
            cnt=ss.count('CD')
            if cnt==160:
                m=max(m,len(ss))
            elif cnt>160:
                break
    print (m)

print (time()-ts)
