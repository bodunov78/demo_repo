def fu(x,a):
    return ((x & 21074 != 0) <= ((x & 12369 == 0) <= (x & a != 0)))


N=len(bin(21074)[2:])

for A in range(0,2**N):
    if all(fu(x,A) for x in range(2**N)):
        print(A)
        break