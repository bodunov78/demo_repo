from itertools import *
t="15,16,26,27,29,35,37,38,48,49,58,67"
g="AB,BV,VD,VK,DK,KI,IJ,JE,EG,EA,GA,GD"
t=t+','+t[::-1]
g=g+','+g[::-1]
L="ABVGDEJIK"
for x in permutations(L):
    # x="".join(x)
    nt=g
    for i,v in enumerate(x,1):
        nt=nt.replace(v,str(i))
        if set(t.split(','))==set(nt.split(',')):
            print (x)
            print (set(t.split(',')))

