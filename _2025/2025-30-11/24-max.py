with open("24-263.txt") as f:
    s=f.readline()
    m=0
    for l in range(len(s)):
        for r in range(l+m,len(s)):
            ss=s[l:r+1]
            if ss.count('Y')<=150:
                m=max(m,len(ss))
            else:
                break
    print (m)