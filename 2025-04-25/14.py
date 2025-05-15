def f(k):
    s=""
    while k>0:
        s=str(k%4)+s
        k=k//4
    return(s.count('0'))



M=0
for x in range(1,3000+1):
    d=4**210+4**110-x
    if f(d)>M:
        M=f(d)
        print(M,x)
