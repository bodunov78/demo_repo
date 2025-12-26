# 14:27
with open("17 (1).txt") as f:
    m=[int(x) for x in f]
    k=[]
    for a,b in zip(m,m[1:]):
        if a*b%3==0 and (a+b)%5==0:
            k.append(a+b)
    print (len(k),max(k))
#14:30