def f(a,b,m):
    if a+b >=47: return m%2 ==0
    if m==0 : return 0
    # останется на 1 камень больше
    h=[f(a+1,b+2,m-1),f(a+2,b+1,m-1),f(a*2,b,m-1),f(a,b*2,m-1)]
    # останется на 1 камень меньше
    # h = [f(a - 1, b, m - 1), f(a, b - 1, m - 1), f(a // 2, b, m - 1), f(a, b // 2, m - 1)]

    return any(h) if (m-1)%2 ==0 else all(h)


print ("19:",[s for s in range(1,36+1) if f(s,10,2) ])
print ("20:",[s for s in range(1,36+1) if (not f(s,10,1)) and f(s,10,3) ])
print ("21:",[s for s in range(1,36+1) if ( f(s,10,2)) or f(s,10,4) ])

