import binascii
import codecs

string = "маша"
hex_representation = bytes(string, 'utf-8').hex()

hex_representation='1'+hex_representation+'3'
print(hex_representation)

hex_representation=hex_representation[1:-1]
result = bytes.fromhex(hex_representation).decode('utf-8')
print(result)