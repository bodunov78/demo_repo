

# print ("AAA"&"BBB")
def xor_two_str(str1, str2):
    return hex(int(str1,16) ^ int(str2,16))
def xare(s,i):
    k = hex(int(i))[2:]
    if len(s) < len(k):
        kk = k[:len(s)]

    else:
        # достариваем ключ до длины текста
        n = len(s) // len(k)
        kk = (k * n).zfill(len(s))
    print("kk", kk)

    # получаем xor текста и числа
    cc = hex(int(s, 16) ^ int(kk, 16))[2:]
    print("cc", cc)
    cc = cc.zfill(len(s))[:len(s)]
    print(cc)

    print(hex(int(cc, 16) ^ int(kk, 16)))
    return cc

# print (bin(int("ABC",16)))
#
# s=bin(int("AAABC",16))[2:]
# # print(len(s),s)
# k='1101'
#
#
# m=int(len(s)/len(k))
# kk=(k*m).zfill(len(s))
# ss=int(s,2)
# kkk=int(kk,2)
# print (s,int(s,2))
# print (kk,int(kk,2))
# c=bin(ss^kkk)[2:].zfill(len(s))
# print (c)
# print(hex(0x12ef ^ 0xabcd))
#
# s="abcde"
# k="1a"
# # генерим ключ по числу
# k=hex(int(input("key:")))[2:]
# print (k,type(k))
# if len(s)<len(k):
#     kk=k[:len(s)]
#
# else:
#     # достариваем ключ до длины текста
#     n=len(s)//len(k)
#     kk=(k*n).zfill(len(s))
# print ("kk",kk)
#
#
# # получаем xor текста и числа
# cc=hex(int(s,16) ^ int(kk,16))[2:]
# print ("cc",cc)
# cc=cc.zfill(len(s))[:len(s)]
# print (cc)
#
#
# print (hex(int(cc,16)^int(kk,16)))
#
#
#

s="1ABCDA0010101"

print (xare(s,777))


