# # считываем N раз числа
# N=int(input())
# for x in range(N):
#     # print (x)
#     d=int(input())
#     print ("D",d)

# считываю числа до 0
# число кратно 5 (делится на 5)
# if d %5==0:
# последняя цифра 6
# if d%10==6:
#
# # 356 //10 35 %10
#
# первая цифра двузначного числа равна 7
# if d//10==7
#
#  первая цифра трехзначного числа равна 5
#  if d//100==5
#
#
#

# средняя цифра трехзначного числа равна 3
# if (d//10)%10 == 3
#
# m=[]
# m.append(d)
#







#
m=[]
d=int(input())
while d !=0:
    print ("DDD",d)
    d=int(input())
    if d%10==7:
        m.append(d)
#

print (m)


# print (m,max(m),len(m),sum(m),sum(m)/len(m))
#
#
#





















# # (1, 2); (11, 2); (1, 12); (11, 12); (−11, −12); (−11, 12); (−12, 11); (10, 10); (10, 5).
# m=((1,2),(11,2),(1,12),(11,12),(-11,-12),(-11,12),(-12,11),(10,10),(10,5))
#
# for a in range(-100,100):
#     cnt=0
#     for s,t in m:
#         if (s > 10) or (t > a):
#             # print ("YES")
#             cnt+=1
#         # else:
#         #     print ("NO")
#     if cnt==7:
#         print (a)
#
#
#
#
#
#
# # x=20
# #
# # while x>1:
# #     print ("Cool Girl",x)
# #     x = x - 3
# #
# #     if x<=10:
# #         break
# #
# #
# #
# #
# # # x=float(input("X:"))
# # # y=float(input("Y:"))
# # #
# # #
# # # if     4<=x<=12  and  5<=y<=10:
# # #     print ("Red")
# # # elif     (-8<=x<=-3  and  7<=y<=9)  or  (-14<=x<=-7  and  5<=y<=6):
# # #     print ("Yellow")
# # #
# # # # elif     -14<=x<=-7  and  5<=y<=6:
# # # #     print ("Yellow")
# # #
# # # elif   (x-8)**2+(y-(-6))**2<=2**2 and (-6<=y<=-2 and   6<=x<=10):
# # #     print ("Brown")
# # #
# # # else:
# # #     print ("Не попал!!!")