
n=1800000
k=0
while k<5:

    a=[]
    nn=n
    for i in range(2,nn):
        if nn%i==0:
            a.append(i)
            while nn%i==0:
                nn=nn//i

    # print (a,nn)
    n+=1
    if len(a)>0 and min(a)+max(a)>10000 and str(min(a)+max(a)).count('3')==2:
        print(a, n,min(a)+max(a))

        k+=1