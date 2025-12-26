from time import *
# for k in range(2):
#     for j in range(3):
#         for i in range(10):

from time import *
ts=time()
cnt=0

for x in ("abcdefgh"):
    for y in ("abcdefgh"):
        for z in ("abcdefgh"):
            s=x+y+z
            if s.count(x)<=2 or s.count(y)<=2:
                cnt+=1
                print (s,cnt)

print (time()-ts)





#
#k=0
# for i in range(0,1000,1):
#     if i%6==0 or i%4==0:
#         print (i)
#
# for i in range(7,1000,10):
#     print  (i)
#
# for i in range(0,1000):
#     if i %10 ==7:
#         print  (i)
#
#
# for i in range(0,1000):
#     j=str(i)[::-1][-1]
#     if j=='5':
#         print (i)








#1--1000

# for i in range(1,1000+1):
#     print(1001-i)


# for i in range(1000,0,-1):
#     print(i)
#
#
# i=1
# while i <=1000:
#     print (1001-i)
#     i+=1
#
# # i=1000
# # while i >0:
# #     print (i)
# #     i-=1
#
