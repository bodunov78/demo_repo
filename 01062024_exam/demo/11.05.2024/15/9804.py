def fu(x,a):
    return (((x&29)!=0) <=(((x&17)==0) <=((x&A) !=0)))



for A in range(0,1000):
    flag=1
    for x in range(0,1000):
        if not fu(x,A):
            flag=0
            break

    if flag==1:
        print(A)
        break