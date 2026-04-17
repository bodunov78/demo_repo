from re import *

s = open('24-215.txt').readline()

reg = r'([ABC][123])+'

m = max((x.group() for x in finditer(reg,s)),key=len)

print(len(m)//2)
print(m)