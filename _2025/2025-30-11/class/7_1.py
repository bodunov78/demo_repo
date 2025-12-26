# Текстовый файл 24-263.txt состоит не более чем из 106 символов и содержит
# только заглавные буквы латинского алфавита. Определите максимальную длину подстроки,
# в которой символ Y встречается не более 150 раз.
from time import *
ts=time()
with open("7_1.txt") as f:
    s=f.readline()
    s=s.strip()

m = 0
for l in range(len(s)):
    for r in range(l + m, len(s)):
        c = s[l:r + 1]
        cnt=c.count('Y')
        if cnt > 150:
            # m = max(m, len(c))
            break
        elif cnt<=150:
            m = max(m, len(c))
            # break
print(m)
print (time()-ts)