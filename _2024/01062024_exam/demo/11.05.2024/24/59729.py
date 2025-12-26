with open("59729.txt") as f:
    s=f.readline().strip()
    m=[i for i in range(len(s)-1) if s[i]==s[i+1]=='T']
    print(m)
    n=[m[i+149]-m[i]+2 for i in range(len(m)-149)]
    print(min(n))

