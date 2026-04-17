from sys import *
from math import *
from functools import *
from itertools import *
from turtle import *
from fnmatch import *
# 1 76216

t="15,16,23,24,27,35,37,46,56"
g="AB,BF,BD,DC,CG,CE,EG,GF,FA"
t=t+','+t[::-1]
g=g+','+g[::-1]

s="ABCDEFG"

for ss in permutations(s):
    nt=g
    for i,v in enumerate(ss,1):
        nt=nt.replace(v,str(i))
    if set(nt.split(','))==set(t.split(',')):
        print (ss)

# c=dict(zip(a,b))


# 2 69907

t="13,18,25,28,34,36,46,57,67,78"
g="DE,EA,EB,AH,HC,HG,CF,FG,GB,BD"
t=t+','+t[::-1]
g=g+','+g[::-1]

s="ABCDEFGH"

for ss in permutations(s):
    nt=g
    for i,v in enumerate(ss):
        nt=nt.replace(v,str(i+1))
    if set(nt.split(','))==set(t.split(',')):
        print (ss)
#
# s='U:\Home\vladimir\Рабочий стол\РОСНЕФТь\Нефтепромлизинг\2025\РН50803599 114 1 2025 Снегоболотоходы\Квалификация'
# print (len(s))


# 2 69907

t="13,15,17,23,24,27,35,36,37,46"
g="AB,BC,CD,AD,DE,DG,DF,EG,GF,AF"
t=t+','+t[::-1]
g=g+','+g[::-1]

s="ABCDEFG"

for ss in permutations(s):
    nt=g
    for i,v in enumerate(ss):
        nt=nt.replace(v,str(i+1))
    if set(nt.split(','))==set(t.split(',')):
        print (ss)
#