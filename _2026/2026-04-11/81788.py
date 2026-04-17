from itertools import *


# проверяем список на условия фано
def fano(s):
    # print ("aaa",s)
    return not(any(a.startswith(b) for a,b in permutations(s,2)))

# получаем все комбинации длиной до n
def variant(n):
    tree = set(["".join(x) for n in range(1, n + 1) for x in product("01", repeat=n)])
    return tree

# выкидываем вырианты не удовлетворяюще услофию фано по известным буквам
def var_k1(k1):
    v = variant(5)
    mn=[x for x in v for k in k1 if x.startswith(k) ]
    M=set(v)-set(mn)-set(k1)
    # print(M,mn)
    return list(M)


#
def vark2(k1,lk2):
    M=var_k1(k1)
    a=[]


    for x in permutations(M, len(lk2)):
        vv=list(x)+k1
        if fano(vv):
            dl2=dict(zip(lk2,list(x)))
            d={**dl1,**dl2}
            # print (list(x),len("".join(d.values())))
            a.append(len("".join(d.values())))
    a.sort()
    print(a[:10])
#     m=[a.startswith(b) for a,b in permutations(x,2) ]
#     if any(m)==False:
#         print (x,any(m),m)
#     # if any(a.startswith(b) for a,b in permutations(x,2) )==[]:
#     #     print (x)
#




# известные буквы
l1=list("ЕЖЗД")

# неизвестные букв
l2=list("АБВГ")

# известный код
k1=list("10,010,011,11".split(','))
# неизвестный код
k2=""

dl1=dict(zip(l1,k1))
print (dl1)

vark2(k1,l2)
# print (M)


# a=":10,:101,В:110,Г:,Д:,Е:"
#
# a=a.replace('0','2')
# m=dict(x.split(':') for x in a.split(','))
# print (dict(m))

# v="0,101,1010,1011,110,1110,1111"
# for x in permutations(v.split(','),6):
#     print (x)
#
#
#
# for a,b in permutations(v.split(','),2):
#     if a.startswith(b):
#         print (a,b)


# v="0,101,1010,1011,110,1110,1111"
# for x in permutations(v.split(','),6):
#     m=[a.startswith(b) for a,b in permutations(x,2) ]
#     if any(m)==False:
#         print (x,any(m),m)
#     # if any(a.startswith(b) for a,b in permutations(x,2) )==[]:
#     #     print (x)
#
# aaa=list("ЕЖЗД")
# ccc=list("10,010,011,11".split(','))
#
# dac=dict(zip(aaa,ccc))
# print (dac)
#
# abv=set(ccc)
# # множдество всех кодов длиной до 5
# tree=set(["".join(x) for n in range(1,5+1) for x in product("01",repeat=n)])
# tree_wo_abv=tree-abv
# # print(len(tree_wo_abv))
# # множкство кодов не удовлетворяющих условию фано по начальным буквам
# tree2={x for x in tree for a in abv if x.startswith(a) }
# tree3=tree-tree2
# print (tree3)
# #
# s=[]
# for x in permutations(tree3,4):
#     # print ("x",list(x)+ccc)
#     # print (type(x),type(s))
#     # s=list(x)+s
#     # print ("sss",s)
#     if fano(list(x)+ccc):
#     # # m=[a.startswith(b) for a,b in permutations(x,2) ]
#     # # if any(m)==False:
#         s.append( [len("".join(list(x)+ccc)),list(x)+ccc])
#     #     # print (x,len("".join(x)),any(m),m)
# #
# # s.sort()
# # print (s)
# # b=set("ЕЖЗД")
# # SS="АБВГДЕЖЗ"
# # V=[]
# # for l,v in s:
# #     k={**dict(zip(b,v)),**dac}
# #     # print (dict(zip(b,v))|dict(dac))
# #     print (k)
# #     nss=SS
#     if fano(k.values()):
#         for key,value in k.items():
#             nss=nss.replace(key,value)
#         V.append((len(nss),list(k.keys()),list(k.values())))
# #
# #
# V.sort()
# print (V)
# #
# #
# # print(len(s),s)
# # m="abcn"
# # n="abcd"
# # if n.startswith(m):
# #     print ("OK")