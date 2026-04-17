from re import *

s = open('файлы к вебу/24-204.txt').readline()

reg = r'(AA|CC)+'

reg = rf'(?=({reg}))'

m = max((x.group(1) for x in finditer(reg,s)),key=len)

print(len(m)//2)
print(m)