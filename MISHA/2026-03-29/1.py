def f3(n,k):
    s=""
    while n>0:
        s=str(n%k)+s
        n=n//k
    return s

def zamena(s):
    s=s.replace('0','z')
    s=s.replace('2','0')
    s = s.replace('z', '2')
    return s


# print (f3(1234,2))
for n in range(1,30):
    s1=f3(n,3)
    s2=zamena(s1)
    print (n,s1,s2)
    # print (n,f3(n,3),zamena(f3(n,3)))