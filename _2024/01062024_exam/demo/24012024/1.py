# N=int(input("Введи N:"))
#
# maxa=-10**19
#
# for i in range(N):
#     x=int(input("Введи X:"))
#     maxa=max(maxa,x)
#     print (i,x,maxa)





N=int(input("Введи N:"))
_Array=[]
maxa=-10**19

# for i in range(N):
#     x=int(input("Введи X:"))
#     if x%5==0:
#         _Array.append(x)
#     # print (i,x,a,max(a))
#
#
# print (max(_Array),min(_Array))

x=int(input("введи число Х"))
while x!=0:
    if x % 5 == 0:
         _Array.append(x)

    x = int(input("введи число Х"))



print (max(_Array),min(_Array),_Array)

