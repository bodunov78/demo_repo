def fu(x,a):
    return (((x&29)!=0) <=(((x&17)==0) <=((x&A) !=0)))



for A in range(0,100):
    # m=[fu(x,A) for x in range(1000)]
    # print (m)
    if all(fu(x,A) for x in range(1000)):
        print(A)
        # break