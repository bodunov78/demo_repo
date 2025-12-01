from time import *

ts=time()

with open("24_21717.txt") as f:
    s=f.readline().strip()
    m=150*3
    a=[]
    for l in range(len(s)):
        for r in range(l+m,len(s)):
            ss=s[l:r+1]
            if ss.count('RSQ')==130 and ss[-1]!='Q':
                a.append(len(ss))
                m=max(m,len(s))
            elif ss.count('RSQ')>130:
                break

    print(min(a))


    m=1000
    a=[]
    for l in range(len(s)):
        for r in range(l+m,l,-1):
            ss=s[l:r+1]
            if ss.count('RSQ')==130 and ss[-1]!='Q':
                a.append(len(ss))
                m=min(m,len(s))
            elif ss.count('RSQ')<150:
                break

    print (min(a))

print (time()-ts)