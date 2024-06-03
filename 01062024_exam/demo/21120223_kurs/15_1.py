m=0
P = [i for i in range(5, 31)]
Q = [i for i in range(14, 24)]
for Amin in range(0, 121):

    for Amax in range(Amin + 1, 121):
        flag=1
        A = [i for i in range(Amin, Amax)]
        # print (f"LEN-{len(A)},A={A}")
        for x in range(1,1000):
            f=((x in P)== (x in Q))<=(not(x in A))
            if not f:
                flag=0
                break
        if flag==1:
            m=max(m,Amax-Amin)
            print (f"Max {m} : {A}")

c=list(range(1,10))
print (c)