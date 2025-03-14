import binascii
import codecs


cnt=0
with open("x.xlsx","rb") as f:
    w=open("xe.txt", "w+")
    for x in f:
        cnt+=1
        print (cnt)
    #     # string = "маша"
    #     x=x.strip()
        hex_representation = x.hex()

        hex_representation='1'+hex_representation+'1'
        w.write(hex_representation)
        # print(hex_representation)
    w.close()

# hex_representation=hex_representation[1:-1]
# result = bytes.fromhex(hex_representation).decode('utf-8')
# print(result)