# Текстовый файл 3.txt состоит не более чем из 10<sup>6</sup> символов и содержит только заглавные буквы латинского алфавита и точки.
# Определите минимальное количество идущих подряд символов, среди которых ровно семь точек.



with open("3.txt") as f:
    s=f.readline()
    s=s.strip()

    # s='11.111111111111.11111111111111111..11111111111111.1111.11111111111111111111111111'
    print (len(s))
    maxi=[]
    dot=[]
    for i,v in enumerate(s):
        if v=='.':
            dot.append(i)
    dot.append(len(s))
    print (dot)
    k=7

    for i in range((k-1),len(dot)):
        lena=dot[i]-dot[i-(k-1)]+1
        print (dot[i],dot[i-(k-1)],i,lena)
        maxi.append(lena)
    print (min(maxi))













k = 0
l = 0
m = []

for r in range(len(s)):
    if s[r]=='.': k += 1

    while k==7:
        m.append(r-l+1)
        if s[l]=='.': k-=1
        l+=1
print(min(m))