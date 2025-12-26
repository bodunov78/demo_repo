from re import *
# with open("24_20909.txt") as f:
#     # for s in f:
#     #     print (len(s))
#
#
#
#
#     s=f.readline()
#
#     AB = r"(AB).*"
#     # numz=r"([1-9][0-9]*|0{1})"
#     abs=rf{AB}{100}
#     proiz = rf"{num}(\*{num})*"
#     reg = rf"(?=({proiz}))"
#     for x in finditer(reg, s):
#         print(x.group(1))
#
#     # s=s.strip()



s="1231231212333112"
ab=r"12[0,2,3,4,5,6,7][0-9]*"
proiz=rf"({ab}){3}"
# reg=rf"(?=({ab}))"
for x in finditer(proiz,s):
    print(x.group(1))
