from sys import *
from math import *
from functools import *
from itertools import *
from turtle import *
from fnmatch import *

def fi(n):
    s=""
    while n>0:
        s=str(n%5)+s
        n=n//5
    return s

for x in range(1,2300):
    if fi(5**100-x).count('0')==3:
        print (x)
        break