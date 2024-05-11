def fu(x,a):
    return ((x & 21074 != 0) <= ((x & 12369 == 0) <= (x & a != 0)))

print (bin(21074)[2:])
N=len(bin(21074)[2:])
print(N)

for A in range(0,2**15):
    flag=1
    for x in range(0,2**15):
        if not fu(x,A):
            flag=0
            break

    if flag==1:
        print(A)
        break
