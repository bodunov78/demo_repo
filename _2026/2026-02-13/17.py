from time import *
ts=time()
a=[]
with open("17.txt") as f:
    for x in f:
        a.append(int(x))
print (a)
# sumik=[]
#
# for i in range(0,len(a)):
#     for j in range(i+1,len(a)):
#         if a[i]%7==0 or a[j]%7==0:
#             if (a[i]%160) != (a[j]%160):
#                 sumik.append(a[i]+a[j])
#
#
# for i in range(1,len(a)):
#     print (a[i-1],a[i])
#
# for i in range(0,len(a)-1):
#     print (a[i],a[i+1])
#39762
a=[1,2,3,4,5,6,7]
cnt=0
for a1,a2 in zip(a,a[::-1]):
    print (a1,a2)
#     if (a1*a2)%15==0 and (a1+a2)%7==0:
#         cnt+=1
#         print (a1,a2)
# print (cnt)
# #
#
# print(len(sumik))
# print (max(sumik))

#     for s in f:
#         a.append(int(s))
#         print (s)
# print(a)
#
# # for x in a[::-1]:
# #     print ("XXX",x)
#
# #37337
# maxi=[]
# for i in range(0,len(a)):
#     for j in range(i+1,len(a)):
#         # print (a[i],a[j])
#         if a[i] % 7 == 0 or a[j] % 7 == 0:
#             if (a[i]%160)!=(a[j]%160):
#
#                 maxi.append(a[i]+a[j])
#
# print (len(maxi),max(maxi))
print (time()-ts)
