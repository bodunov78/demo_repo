from re import *

s = open('24-332.txt').readline()

word = r'([ABCabc][abc]*)'

word1 = r'([ABC][abc]*)'

pred = rf'{word1}( {word})+\.'

m = max((x.group() for x in finditer(pred,s)),key=len)

print(len(m))
print(m)