from re import *

s = open('k7a-3.txt').readline()

reg = r'[ABEF]+'

m = max((x.group() for x in finditer(reg,s)), key=len)

print(len(m))
print(m)