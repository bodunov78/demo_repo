from time import *
ts=time()
def f1(s):
    m = 100_000
    for l in range(len(s)):
        for r in range(l + m, len(s)):
            ss = s[l:r + 1]
            cnt = ss.count('CD')
            if cnt == 160:
                m = max(m, len(ss))
            elif cnt > 160:
                break
    return m


with open("24_17535.txt") as f:
    s=f.readline()
    print(len(s))
    s=s+"CD"
    # f1(s)
    ind=[]
    k=[]
    for i in range(len(s)-1):
        if s[i]=='C' and s[i+1]=='D':
            ind.append(i+1)
    print (len(ind))
    print (ind[:160])
    for i in range(160,len(ind)-1):
        if i!=160:
            ss=s[ind[i-160-1]:ind[i]-1+1]
            print(ss.count('CD'), len(ss),s[ind[i-160-1]],s[ind[i]-1] )
            k.append(len(ss))
            break
        elif i==160:
            # e=ind[i+1]
            ss=s[0:ind[i]-1]
            print (ss.count('CD'),len(ss))
            k.append(len(ss))
        # k.append(f1(ss))

    print (max(k))
    #

print (time()-ts)
