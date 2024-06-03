a=[]
try:
    with open("9_27517.csv","r") as file:

        for s in file:
            print(s)




except:
    print ("Error")




#
#
#
#
# with (open("9_27517.csv","r") as file):
#     for x in file.readlines():
#         m=list(map(str,x.strip().split(';')))
#         #print(m)
#
#         for y in m[1:]:
#             if y != '':
#                 y=y.replace(",",".")
#                 a.append(float(y))
#         #
#         #     print (i,y)
#         # #     if i >0:
#         #         m[i]=int(y)
#         # print (m)
# print(sum(a)/len(a))
# print(a)