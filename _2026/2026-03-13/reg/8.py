from re import *

s = open('файлы к вебу/24-264.txt').readline()

reg = r'[1-9A-F][0-9A-F]*'
reg = rf'(?=({reg}))'

m = max((x.group(1) for x in finditer(reg,s)),key=len)

print(len(m))
print(m)