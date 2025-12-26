import binascii
import codecs



with open("teste.dat") as f:
    w=open("testd.dat","w+")
    for x in f:
        # print (x)

        # hex_representation='1'+hex_representation+'3'
        result = bytes.fromhex(x).decode('utf-8')
        w.write(result)
        # print(hex_representation)

    w.close()
    
# hex_representation=hex_representation[1:-1]
# result = bytes.fromhex(hex_representation).decode('utf-8')
# print(result)