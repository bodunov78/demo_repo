from time import *

ts=time()

with open("24_21717.txt") as f:
    s=f.readline()
    m = 10000
    for l in range(len(s)):
        for r in range(l + m, l, -1):
            c = s[l:r + 1]
            if c.count('RSQ') >= 130 and c[-1]!='Q':
                m = min(m, len(c))
            else:
                break
    print(m)

print (time()-ts)