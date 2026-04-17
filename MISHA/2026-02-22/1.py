def des2n(n,k):
    s = ""
    L="0123456789ABCDEFGH"
    while n > 0:
        ost = n % k
        s = L[ost] + s
        n = n // k
        print(ost)
    # print(s)
    return s
S=des2n(2222,16)
print (S,oct(2222)[2:])





# for i in range(0,20+1):
#     print (i,2**i)
#
# print (bin(213)[2:],oct(213)[2:],hex(213)[2])


# print (213%7)
# print (213//7)
# print (30%7)
# print (30//7)
# print (4%7)
# print (int("423",7))

# n=213
# s=""
# while n>0:
#     ost=n%7
#     s=str(ost)+s
#     n=n//7
#     print (ost)
# print (s)

# проверяем десятичной с-мой





# 11010101 = 1*2^0 + 0*2^1 +1*2^2+0*2^3+1*2^4+0*2^5+1*2^6+1*2^7
# 1+4+16+64+128=213
# print (bin(213))
# 213-128=85-64=21-16=5-4=1-1=0
# 11010101

