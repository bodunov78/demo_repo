from re import *
# for i in range(0,10**9,23):
#     # reg=rf"(12345[0-9]7)*)"
#     pattern = r'^12345\d7\d8$'
#     reg = rf'(?=({reg}))'
#     if findall(pattern, str(i)):
#         print (i)


with open("24 (2).txt") as f:
    s=f.readline()
    s=s.strip()
    pattern = r'(W.*W)'
    pattern = rf'(?=({pattern}))'
    for x in finditer(pattern, s):
        s=x.group(1)
        if s.count('W')>130:
            continue
        elif s.count('W')==130:
            print (len(s),s.count('W'))
