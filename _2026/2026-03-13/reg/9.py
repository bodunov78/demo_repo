from re import *

s = open('файлы к вебу/24-319.txt').readline()

numb = r'([1-9][0-9]*|0)'

reg = rf'{numb}([-*]{numb})+'

m = max((x.group() for x in finditer(reg,s)),key=len)

print(len(m))
print(m)