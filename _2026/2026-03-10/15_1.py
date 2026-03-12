def z15(x,a):
    def treug(n,m,k):
        if max(n,m,k)<(n+m+k -max(n,m,k)): return 1
        else: return 0
    def maxa(a,b):
        if a>b: return a
        else: return b

    if not(treug(x,11,16)==(not(maxa(x,5)>10)) and (treug(4,a,x))):
        return 1
    else:
        return 0

for a in range(1,100):
    m=[z15(x,a) for x in range(1,100)]
    if all(m):
        print (a)