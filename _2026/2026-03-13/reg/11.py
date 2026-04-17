from re import *

s = open('файлы к вебу/24-299.txt').readline()

numb = r'([1-9][0-9]*|0)'

prod = rf'(({numb}\*)*0(\*{numb})*)'

reg = rf'{prod}(\+{prod})+'

m = max((x.group() for x in finditer(reg,s)), key=len)

print(len(m))
print(m)