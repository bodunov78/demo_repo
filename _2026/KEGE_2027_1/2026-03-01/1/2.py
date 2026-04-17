# # a=(1,2,3)
# # b=[1,2,3]
# # c={1,2,3}
# # d=range(1,100,1)
# # print (type(a),type(b),type(c),type(d))
# print (20*30+50/4%40//2)
# print (249&240)
# print (bin(249)[2:])
# print (bin(240)[2:])
# print (249^240)
# print (3999//345)
# print (int(2222.444))
# # print (int("ABC4",9))
# print (int('36',9))
# print (bin(33))
# print (33//2//2)
# #
# # 11 == 4
# # 10 == 4
# # ctrl+/
from string import *
# print (printable)
def f1(n,k):
    L=printable
    # print (L[15])
    s=""
    while n>0:
        ost=n%k
        s=L[ost]+s
        n=n//k
    # print (s)
    return s

ggg=f1(255,27)
print (f1(253,16))