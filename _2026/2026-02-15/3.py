s="abcd"
s=list(s)
for a in s:
    m=a
    s1=s
    s1.remove(a)
    for b in s1:
       m2=m+b
       s2=s1
       s2.remove(b)
       for c in s2:
           m3=c
           m3=m2+c
           s2.remove(c)
           print (m3)
