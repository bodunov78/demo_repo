s="qwertyuiop"
arr=[3,33,4,5,6,33,99,-1]
# arrb=['aaa','asss','ssss']
# # arra={1:2}
# # print(max(arr),min(arr),sum(arr)/len(arr))
# # arr.sort(reverse=1)
# print (arr)
# arr.append(777)
# arr.insert(4,888)
# # arr.remove(33)
# x=arr.pop(-1)
# print (x)
# print (arr)
#
# if 5 in arr:
#     print (*arr)
#
# while 33 in arr:
#     arr.remove(33)
# print (arr)
#
# for x in arr:
#     print (x**2)
#
# for i in range(len(arr)):
#     print (i,arr[i])

for i,v in enumerate(arr):
    if v%2==1:
        arr[i]+=1000
print (arr)

# a=[-1,1,2,3,5,8,13,21,34]
# for i in range(len(a)):
#     for j in range(i+1,len(a)):
#         print (a[i],a[j])
from time import *
from math import *
ts=time()
a=[]
for i in range(1,10**7):
    if 13*i>10**7:
        break
    a.append(13*i)
print (a)
print (time()-ts)

12 3 5 7 9 66

a=4
b=7

a,b = b,a
