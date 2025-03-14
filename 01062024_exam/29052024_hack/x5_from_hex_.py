import binascii
import codecs


cnt=0
s=""
with open("xe.txt") as f:
    w=open("x_d.xlsx","wb+")
    for x in f:
        cnt+=1
        print(cnt)
        # print (x)
        x=x.strip()
        x=x[1:-1]
        s=s+x
        # hex_representation='1'+hex_representation+'3'
        # result = bytes.fromhex(x).decode('utf-8')
    result = bytes.fromhex(s)

        # print(result)
    w.write(result)
        # print(hex_representation)

    w.close()
    
# hex_representation=hex_representation[1:-1]
# result = bytes.fromhex(hex_representation).decode('utf-8')
# print(result)