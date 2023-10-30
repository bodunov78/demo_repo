# # s="12,34:56,78,9,10"
# # # s="12,34.2,56"
# # print (s[1:3])
# #
# #
# #
# #
# # a=list(s.replace(',',':').split(':'))
# # print(a)
# #
# # a=list(map(int,a))
# # print (a)
# #
# # print(min(a),max(a))
# # # a.sort(reverse=1)
# # # a=a[::-1]
# # # b=a[:]
# # b=a.copy()
# #
# # print (b)
# # b[0]=100000
# # print(b)
# # print (id(a),id(b))
# # print(a)
# from itertools import *
# a=[[1,2,3,4],[5,6,7,8],[9,0,1,2]]
# print (a)
# for x in a:
#     print (x)
#
# b=list(zip(*a))
#
# for x in b:
#     print (x)
#
# s="0123456789ABCDEF"
# n=65535
# ch=""
# while n>0:
#     ost=s[n%16]
#     n=n//16
#     ch=str(ost)+ch
# print (ch,int(ch,16))
#


#
#
#
# a[2][0]=999
#
# for x in a:
#     print (x)
#     for y in x:
#         print (y)
#
#
#



# for i,e in enumerate(a):
#     if e.isdigit():
#         a[i]=float(e)
# a="москва:1000"




# print(a)

from itertools import *
# a=[]
# s="0123456789ABCDEF"
# for x in product(s,repeat=6):
#     a.append("".join(x))
# print (a[1000])

#Возвращает подпоследовательности длины r из элементов итерируемого объекта, подаваемого на вход.
s=[1,2,3,4]
# a=[]
# for i in range(1,4):
#     for x in combinations(s,i):
#         a.append(sum(x))
#         # print (x,sum(x))
# print (len(a),len(set(a)),set(a))

for x in permutations(s,2):
    print (x)

suma=0
lena=0
mina=1000
maxa=-1000
cnt=0
with open("9_27520.csv",encoding="utf-8-sig") as file:
    for x in file:
        # print (x.strip().replace(',','.').split(';')[:-2])
        a=list(map(float,x.strip().replace(',','.').split(';')[:-2]))
        for i in range(len(a)):
            if a[i] <20:
                cnt+=1

        # mina=min(min(a),mina)
        # maxa=max(max(a),maxa)
        # # suma+=sum(a)
        # # lena+=len(a)

print(mina,maxa,cnt)


print (a)