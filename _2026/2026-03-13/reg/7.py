from re import *

s = open('файлы к вебу/24-263.txt').readline()

reg = r'Z([^Z]*Z){119}'
reg = rf'(?=({reg}))'

m = min((x.group(1) for x in finditer(reg,s)),key=len)

print(len(m))