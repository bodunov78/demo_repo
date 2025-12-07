# x&21074 ≠ 0 → (x&12369=0 → x&A ≠ 0)

# def fi1(x,a):
#     # return (x&21074!=0) <=((x&12369)<=((x&a)!=0) )
#     return ((x & 21074 != 0) <= ((x & 12369 == 0) <= (x & a != 0)))
#


# долго
# for a in range(16000, 10**5):
#     m=all([fi1(x,a) for x in range(100_000)])
#     if m:
#         print(a)
#         break


# for a in range(0, 10**5):
#     k = True
#     for x in range(0, 10**5):
#         if ((x & 21074 != 0) <= ((x & 12369 == 0) <= (x & a != 0)))==0:
#             k = False
#             break
#     if k == True:
#         print(a)
#         break







#Тип 15 34541
#!!!!!!!!!!!!!!!!!!!!!!
#
#
#
#
#
#
# def frange(a,b,c):
#     x=a
#     m=[]
#     while x<b:
#         m.append(x)
#         x+=c
#
#     return m
#
#
# P=[x for x in frange(3,38+0.5,0.5)]
# Q=[x for x in frange(21,57+0.5,0.5)]
#
# R=[x for x in frange(35,50+0.5,0.5)]
#
# vA=[x for x in frange(0,100+0.5,0.5)]
# d=[]
#
#
# a = []
# maxa=-10**19
#
# for nach in range(len(vA)-1):
#     for kon in range(nach+1,len(vA)):
#         #print (nach,kon)
#         A=vA[nach:kon]
#         #print (m)
#         if all( (((x in Q)<=(x in P))<=(not (x in A))) for x in frange(0,100,0.5)  ):
#             if len(A)>maxa:
#                 print(len(A),A)
#                 maxa=len(A)

#68248
for a in range(0, 1000):
    k = True
    for x in range(0, 1000):
        for y in range(0, 1000):
            if (((y < 20 ) <= ( x > 70)) or (not((x < a)) <= (y > a))) == 0:
                k = False
                break
        if k == False:
            break
    if k == True:
        print(a)
        break