# Текстовый файл 0.txt содержит строку из заглавных латинских букв и точек, всего не более 106 символов.
# Определите максимальное количество идущих подряд символов, среди которых не более пяти точек.
with open("0.txt") as f:
    s=f.readline()
    s=s.strip()
    dot=[-1]

    # s='11.111111111111.11111111111111111..11111111111111.1111.11111111111111111111111111'
    print (len(s))
    maxi=[]
    for i,v in enumerate(s):
        if v=='.':
            dot.append(i)
    dot.append(len(s))
    print (dot)
    for i in range(3,len(dot)):
        lena=dot[i]-dot[i-3]+1-2
        print (dot[i],dot[i-3],i,lena)
        maxi.append(lena)
    print (max(maxi))





    k = 0
    l = 0
    m = []
    for r in range(len(s)):
        if s[r]=='.': k += 1
        while k>2:
            if s[l]=='.': k-=1
            l+=1
        if k<=2:
            m.append((r-l+1,r,l))

    print(max(m))