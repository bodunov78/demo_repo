from re import *

s = open('24-215.txt').readline()
print (s)
reg = r'(?=( ([ABC][123][ABC])+ ))'.replace(' ','')
for x in finditer(reg,s):
    print (x.group())
# m = [(x.group(1) for x in finditer(reg,s))]
#
# print(len(m)//3)
# print(m)