with open("24-s2.txt") as f:
    s=f.readline()
    d={}
    for i in range(len(s)-1):
        if s[i]=='X':
            v=d.get(s[i+1],0)
            d[s[i+1]]=v+1


    for x in d:
        print (x,d[x]  if d[x]==max(d.values()) else "")