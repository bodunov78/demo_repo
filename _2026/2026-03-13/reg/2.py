from re import *

s = open('файлы к вебу/k7a-6.txt').readline()

reg = r'[^AE]+'

m = max((x.group() for x in finditer(reg,s)), key=len)

print(len(m))
print(m)