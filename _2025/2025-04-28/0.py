from fnmatch import *
from re import *

a='12543 -1243 1233777343'
# pat=r'\b[-\d{5}\b?'
#
# match = findall(r'-\d\d\d43\b|\b\d\d\d43\b', a)
# if match:
#     print(match)

a="111343"
# a=['-12345','23456']
b=['12343','123432']

pat="[!-]????"
pat2="[!-]????"
pat3="[!-]????,-?????"
pat4="^\D*\d{5}\D*$"
pat5="^[\D*,-]\d{5}\D*$"
pat6="^-\d{3}43$|^\d{3}43$"
# if fnmatch(a,pat) or fnmatch(a,pat2):
#     print(a)
# if filter(a,pat):
#     print(filter(a,pat3))

# if match(pat6,a):
#     print(match(pat4,a))
k=[str(a) for a in range(-99999,100000) if len(str(abs(a)))==5 and str(a)[-2:]=='43']
print (len(k))

if any(1 if x in k else 0 for x in b):
    print (b,"for")

if any(1 if match(pat6,x) else 0 for x in b):
    print (b)
