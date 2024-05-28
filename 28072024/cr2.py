import binascii
import codecs



with open("te2.txt","rb") as f:
    w=open("te2e.txt", "w+")
    for x in f:
        print (x)
    #     # string = "маша"
        x=x.strip()
        hex_representation = x.hex()

        # hex_representation='1'+hex_representation+'3'
        w.write(hex_representation)
        # print(hex_representation)
    w.close()

# hex_representation=hex_representation[1:-1]
# result = bytes.fromhex(hex_representation).decode('utf-8')
# print(result)