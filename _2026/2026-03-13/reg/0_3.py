from re import *
# s="то-либо кто-то что-то то-ли где-то что"
# reg=r'(\w?)то-'
# for x in finditer(reg,s):
#     print (x.group())

s="234567"
reg=r'\d\d'

# reg=rf"(?={reg})"
reg = rf'(?=({reg}))' # пересечение
for x in findall(reg,s):
    print (x)


s="то-либо кто-то что-то то-ли где-то что"
reg=r"\bто-\w+|\w+-то\b"
# reg = rf'(?=({reg}))' # пересечение
for x in findall(reg,s):
    print (x)
