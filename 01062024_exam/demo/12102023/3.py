# # 0,1,2,3
# arr=[]
# arr2=[]
# for i in (1,2,3):
#     for j in (0,1,2,3):
#         for k in (0,1,2,3):
#             if i+k >j:
#                 arr.append((i,j,k))
#                 print (i,j,k)
# print (len(arr),arr)
#
# for i in "123":
#     for j in "0123":
#         for k in "0123":
#             if int(i)+int(k)> int(j):
#                 print (i+j+k)
#                 arr2.append(i+j+k)
# print (len(arr2))

# for i in range(12345678,13345679,3):
#     print (i,str(i)[:-1]) # кроме последнего
#     print(i, str(i)[1:-1]) # кроме первого и последнего
#     print(i, str(i)[1:]) # кроме первого

from itertools import *
a="12345"
arr=[]
for x in product(a,repeat=5):
    print (x)
    s="".join(x)

    if s.count("1")==1 and s.count("2")==1 and s.count("3")==1 and s.count("4")==1 and s.count("5")==1 :
        arr.append(s)

print (arr,'\n',len(arr))



