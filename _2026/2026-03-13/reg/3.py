from re import *

s = open('24-213.txt').readline()

reg = r'(NPO|PNO)+'

m = max((x.group() for x in finditer(reg,s)),key=len)

print(len(m)//3)
print(m)