s = open('24-181.txt').readline()

k = 0
l = 0
m = []
for r in range(len(s)):
    if s[r]=='.': k += 1
    while k>2:
        if s[l]=='.': k-=1
        l+=1
    if k<=5:
        m.append(r-l+1)

print(max(m))

