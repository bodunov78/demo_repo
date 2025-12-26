# from sys import *
# from math import *
# from functools import *
# from itertools import *
# from turtle import *
# from fnmatch import *
# максимальная строка содержащая 85 последовтельностей GSW
# with open("1004_24.txt") as f :
#     s=f.readline().strip()
#     m=85*3
#     maxi=m
#     for l in range(len(s)):
#         for r in range(l+m,len(s)):
#             ss=s[l:r+1]
#             if ss.count('GSW')==85 and ss[-3:]=='GSW':
#                 maxi=max(maxi,len(ss))
#                 m=maxi
#             elif ss.count('GSW')>85:
#                 break
#     print (maxi)

# минимальная длина строки содержащая 130 RSQ и не заканчивающаяся на Q
# with open("24_21717.txt") as f:
#     s=f.readline()
#     m = 10000
#     for l in range(len(s)):
#         for r in range(l + m, l, -1):
#             c = s[l:r + 1]
#             if c.count('RSQ') >= 130 and c[-1]!='Q':
#                 m = min(m, len(c))
#             else:
#                 break
#     print(m)