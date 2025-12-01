from time import *
ts=time()
with open("81490.txt") as f:
    s=f.readline()
    m=0
    am=[]
    for l in range(len(s)):
        for r in range(l+m,len(s)):
            ss=s[l:r+1]
            if  ss[:4]=='2025' and ss.count('Y')>=120 and ss.count('2025')==60:
                    am.append((len(ss),ss))
                    m = max(m, len(ss))
            elif ss.count('2025')>60:
                break

    print (m)


    print (len(max(am)),max(am))

print (time()-ts)