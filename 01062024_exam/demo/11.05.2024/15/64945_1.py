def fu(x,a):
    # return ((x & 21074 != 0) <= ((x & 12369 == 0) <= (x & a != 0)))
    return (((x & 21074) != 0) <= (  (x & 12369) == 0 <=( (x & a) != 0)))


N=len(bin(21074)[2:])

for A in range(0,2**N):
    flag=1
    for x in range(0,2**N):
        if not fu(x,A):
            flag=0
            break

    if flag==1:
        print(A)
        break
