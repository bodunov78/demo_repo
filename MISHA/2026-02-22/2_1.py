# # 88x4y9   x44y11.
# for x in range(0,8+1):
#     for y in range(0,8+1):
#         a=f"88{x}4{y}"
#         # print (a)
#         a=int(a,9)
#         b=f"7{x}44{y}"
#         b=int(b,11)
#         if (a+b)%61==0:
#             print (a+b,(a+b)//61,a,b)

from itertools import *
# for x,y in product("012345678",repeat=2):
#     a=f"88{x}4{y}"
#     # print (a)
#     a=int(a,9)
#     b=f"7{x}44{y}"
#     b=int(b,11)
#     if (a+b)%61==0:
#         print (a+b,(a+b)//61,a,b)
# for a in product([0,1],repeat=4):
#     print (a[1],a[2],a[3],a[-1])

for x in "0123456789AB":
    for y in "0123456789AB":
        a=f"10{x}234{y}"
        print (a,int(a,12))

