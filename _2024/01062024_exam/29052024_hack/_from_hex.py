import binascii
import codecs
from random import *
from time import *
def xare(s,i):
    k = hex(int(i))[2:]
    if len(s) < len(k):
        kk = k[:len(s)]

    else:
        # достариваем ключ до длины текста
        n = len(s) // len(k)
        kk = (k * n).zfill(len(s))
    #print("kk", kk)

    # получаем xor текста и числа
    cc = hex(int(s, 16) ^ int(kk, 16))[2:]
    #print("cc", cc)
    cc = cc.zfill(len(s))[:len(s)]
    #print(cc)

    #print(hex(int(cc, 16) ^ int(kk, 16)))
    return cc


def frange(n,e,s):
    fname=f"C:\\{n}\\{e}.txt"
    with open(fname, "r") as f:
        w = open(f"{e}_d.txt", "wb+")
        for x in f:
            # cnt += 1
            # print(cnt)
        #     # string = "маша"
            x = x.strip()
            chex = xare(x, s)
            chex = chex[1:-1]
            result = bytes.fromhex(chex)
            w.write(result)

        # print(hex_representation)
        w.close()





    return fname


def adsn():
    cnt = 0
    with open("19.txt", "r") as f:
        w = open("19_de.txt", "wb+")
        for x in f:
            cnt += 1
            print(cnt)
        #     # string = "маша"
            x = x.strip()
            chex = xare(x, 777)
            chex = chex[1:-1]
            result = bytes.fromhex(chex)
            w.write(result)

        # print(hex_representation)
        w.close()


# hex_representation=hex_representation[1:-1]
# result = bytes.fromhex(hex_representation).decode('utf-8')
# print(result)


#print (process_time_ns())