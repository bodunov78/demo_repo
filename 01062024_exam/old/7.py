import csv
from math import *
from itertools import *
from fnmatch import *
from csv import reader


with open("1.csv") as F:
    # s = reader(F, delimiter=';', quotechar='"')
    s = reader(F, delimiter=';', quotechar= '"')

    for row in s:
        print(', '.join(row))


f=open("1.py","r")
a=[x for x in f.readlines()]
print (a)



for y in product("ABC",repeat=2):
    print (y)
for x in permutations('abc'):
    print (("").join(x))



#print(abc)

































































print("Fuck")
