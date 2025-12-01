from itertools import *
from fnmatch import *
from functools import *
from math import *
from pickle import *
from sys import *
# setrecursionlimit(100000)


from functools import *

def f(s,e):
    if s==e:return 1
    elif s<e or s==18 : return 0
    else : return f(s-2,e)+f(s-4,e)+f(s//3,e)

# 37 29 19 16

print (f(37,29)*f(29,19)*f(19,6))

