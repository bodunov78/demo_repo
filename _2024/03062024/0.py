# from oss import *
import binascii
import codecs
from random import *
from time import *
from os import *


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

    fname=f"C:\\{n}\\{e}.log"
    print(n,e,s,fname)
    f=open(fname, "r")
    w = open(f"{e}.py", "wb+")
    for x in f:
        x = x.strip()
        chex = xare(x, s)
        chex = chex[1:-1]
        result = bytes.fromhex(chex)
        w.write(result)

        # print(hex_representation)
        w.close()
    return 1

def fff():
    if e==999:
        d = listdir("C:\\1\\")

        for x in d:
            if ".log" in x:
                ee=int(x.replace(".log",""))
                print (x,e)
                fname = f"C:\\{n}\\{ee}.log"
                print (type(fname),fname)
                with open(fname, "r") as f:
                    w = open(f"{e}.py", "wb+")
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

                print(x)



print (frange(1,2,777))
