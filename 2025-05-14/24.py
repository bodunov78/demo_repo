#12:38

with open("24_19254.txt") as f:
    s=f.readline()
    s=s.strip()
    a=[]
    maxi=4*80
    for l in range(0,len(s)):
        for r in range(l+maxi,len(s)):
            if s[l:r+1].count('FSRQ')==80:
                maxi=max(maxi,len(s[l:r+1]))
            if s[l:r+1].count('FSRQ')>80:
                break

    print (maxi)

    #12:43
