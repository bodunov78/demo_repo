from itertools import *
s='101110011111110101'
m=[('1101','Т'),('0011','Р'),('111','О'),('000','К'),('10','В'),('01','А')]
for x in permutations(m):
    s = '101110011111110101'
    for f,t in x:
        s=s.replace(f,t)
    print (s,x)
#         if '1' not in s and '0' not in s:
#             print (s)
#
# s='101110011111110101'
# s=s.replace('1101','Т').replace('0011','Р').replace('111','О').replace('000','К').replace('10','В').replace('01','А')
# print (s)