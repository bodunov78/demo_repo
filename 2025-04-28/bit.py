c=input()
if c[0] in 'ACEG':
    k=0
else:
    k=1

if c[1] in '1357':
    k=k+0
else:
    k=k+1

k=k%2
if k==1:
    print("WHITE")
else:
    print("BLACK")

# a=int(input())
# b=bin(a)[2:].count('1')
# print(b)
# # n,k =input().split()
#
# n=int(n)
# k=int(k)
#
# a=""
# while n >0:7
#     a=str(n%k)+a
#     n=n//k
# s=0
# m=1
# for c in a:
#     s+=int(c)
#     m*=int(c)
# print (m-s)
#
#
#
#
# # from string import *
# # b=input()
# # a="0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
# # c=0
# # for d in b:
# #     if d in a:
# #         c=max(c,a.index(d)+1)
# #     else:
# #         c=-1
# #         break
# #
# # print (c)
#
# # b=sorted(b)
# # if len(set(b)-set(a))>0:
# #     b=-1
# # else:
# #     b = a.index(b[-1])+1
# # print (b)
#
# # a=int(input())
# # b=bin(a)[2:][::-1]
# # print (int(b,2))
