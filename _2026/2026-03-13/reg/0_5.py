from re import *
# s="то-либо кто-то что-то то-ли где-то что"
# reg=r'(\w?)то-'
# for x in finditer(reg,s):
#     print (x.group())

L="0123456789"
print (L[::2])
reg=rf'(([{L[::2]}][{L[1::2]}]))'
s="11223334567777788"
reg=r'[2347]*'
reg=rf"(?={reg})"
# reg = rf'(?=({reg}))' # пересечение
for x in findall(reg,s):
    print (x)

#
# s="то-либо кто-то что-то то-ли где-то что"
# reg=r"\bто-\w+|\w+-то\b"
# # reg = rf'(?=({reg}))' # пересечение
# for x in findall(reg,s):
#     print (x)
#
#
# with open("10.txt",encoding='utf-8') as f:
#     for s in f:
#         # print (s)
#         s=s.strip()
#         # reg = r"\bто-\w+|\w+-то\b"
#         # reg = r"\долг\b|олг\b"
#         # reg = r"\bчто-|\bЧто-|-что|-Что\b"
#         reg = r'\b[а-яё]*то[а-яё]*\b'
#         reg = rf'(?i)(?=({reg}))'  # пересечение , (?i) игнорировать регистр
#         if findall(reg,s):
#             print (s,findall(reg,s))
