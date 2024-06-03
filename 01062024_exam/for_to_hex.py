import binascii
import codecs
from random import *
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


cnt=0

k=[2,6,61,8,9,11,12,13,14,15,16,17,19,20,21,23,25,251,221]
for i in k:
    sname=f"{i}.py"
    dname=f"C:\\1\\{i}.log"
    with open(sname,"rb") as f:
        w=open(dname, "w+")
        for x in f:
            cnt+=1
            print (cnt)
    #     # string = "маша"
    #     x=x.strip()
            hex_representation = x.hex()

            hex_representation=str(randint(0,9))+hex_representation+str(randint(0,9))
            chex=xare(hex_representation,777)
            w.write(chex+'\n')

        # print(hex_representation)
        w.close()

# hex_representation=hex_representation[1:-1]
# result = bytes.fromhex(hex_representation).decode('utf-8')
# print(result)