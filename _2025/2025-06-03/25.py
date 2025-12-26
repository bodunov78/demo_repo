def deli(n):
    m=dict()
    for i in range(2,n):
        if n%i==0:
            k=0
            while n%i==0:
               k+=1
               n=n//i
            m[i]=k
    return m



print (deli(18000000))

for i in range(18000000,18000010):

    for k,v in deli(18000).items():
        print (i,k,v)