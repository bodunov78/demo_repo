import binascii
import codecs



with open("te2e.txt") as f:
    w=open("te2d.txt","wb+")
    for x in f:
        # print (x)

        # hex_representation='1'+hex_representation+'3'
        # result = bytes.fromhex(x).decode('utf-8')
        result = bytes.fromhex(x)

        # print(result)
        w.write(result)
        # print(hex_representation)

    w.close()
    
# hex_representation=hex_representation[1:-1]
# result = bytes.fromhex(hex_representation).decode('utf-8')
# print(result)