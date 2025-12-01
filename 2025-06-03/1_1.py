from itertools import *
t='14,15,17,24,26,35,36,37,56'
g="AB,BD,DG,DF,FG,FE,EC,CG,CA"

t=t+','+t[::-1]
g=g+','+g[::-1]
s="ABCDEFG"

for p in permutations(s):
    nt=g
    for i,v in enumerate(p):
        nt=nt.replace(v,str(i+1))
    if set(t.split(','))==set(nt.split(',')):

        print (p)
        print ([str(i)+"" for i in range(1,8)])
        print(8+30)
