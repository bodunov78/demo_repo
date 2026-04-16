from itertools import *



def fano(s):
    return not(any(a.startswith(b) for a,b in permutations(s,2)))




a="А:0,Б:101,В:110,Г:,Д:,Е:"

a=a.replace('0','2')
m=dict(x.split(':') for x in a.split(','))
print (dict(m))

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

aaa=list("АБВ")
ccc=list("0,101,110".split(','))

dac=dict(zip(aaa,ccc))
print (dac)

abv={'0','101','110'}
# множдество всех кодов длиной до 5
tree=set(["".join(x) for n in range(1,5+1) for x in product("01",repeat=n)])
tree_wo_abv=tree-abv
# print(len(tree_wo_abv))
# множкство кодов не удовлетворяющих условию фано по начальным буквам
tree2={x for x in tree for a in abv if x.startswith(a) }
tree3=tree-tree2
# print (tree3)

s=[]
for x in permutations(tree3,3):
    m=[a.startswith(b) for a,b in permutations(x,2) ]
    if any(m)==False:
        s.append( (len("".join(x)),x))
        # print (x,len("".join(x)),any(m),m)

# s.sort()
b=set("ГДЕ")
SS="АБВГДЕ"
V=[]
for l,v in s:
    k={**dict(zip(b,v)),**dac}
    # print (dict(zip(b,v))|dict(dac))
    print (k)
    nss=SS
    if fano(k.values()):
        for key,value in k.items():
            nss=nss.replace(key,value)
        V.append((len(nss),list(k.keys()),list(k.values())))


V.sort()
print (V)
#
#
# print(len(s),s)
# m="abcn"
# n="abcd"
# if n.startswith(m):
#     print ("OK")