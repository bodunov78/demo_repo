
#10954
a=((2,-2),(5,3),(14,1),(-12,5),(5,7),(10,3),(8,2),(3,0),(-4,9))

# (2, –2); (5, 3); (14, 1); (–12, 5); (5, 7); (10, 3); (8, 2); (3, 0); (–4, 9).
cnt=0
for s ,t in a:
    if s > -4 or t <3 :
        print("YES")
        cnt+=1
    else:
        print("NO")

print("cNT",cnt)
#37331
m=((1,2),(11,2),(1,12),(11,12),(-11,-12),(-11,12),(-12,11),(10,10),(10,5))
for A in range(100):
    cnt=0
    for s ,t in m:
        if s > 10 or t > A:
           # print("YES")
           cnt+=1
        # else:
        #     print("NO")

    if cnt==7:
        print ("A",A)














# # 200 300 шаг 1
# # i=200
# # while i < 300:
# #     print (i)
# #     i=i+2
#
#
# # 300 -200 шаг 5
# # i=301
# # while i >= -200:
# #     print (i)
# #     i=i-5
# #     if i >=0:
# #         break
# i=0
# while i < 4:
#     for x in ("Маша","Наташа","Светлана","Екатерина","Анюта","Люся"):
#         print (x)
#         if x == "Наташа":
#             i=4
#             break
#
#     i=i+1