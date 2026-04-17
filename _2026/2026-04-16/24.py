with open("24_2.txt") as f:
    # s = open('24_26491.txt',"r").readline()
    s=f.readline()
    mx_len = 0
    print(len(s))
    for l in range(len(s)):
        for r in range(l + mx_len, len(s)):
            pst = s[l:r+1]
            if pst[0] in '0+*' or '*0' in pst.replace('+', '*') or '**' in pst.replace('+', '*'):
                break
            if pst[-1] not in '+*' and eval(pst) % 2 != 0:
                mx_len = max(mx_len, len(pst))
                if mx_len==247:
                    print (pst)
    print(mx_len)