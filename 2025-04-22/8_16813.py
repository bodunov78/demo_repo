from itertools import *
cnt=0
for x in permutations("ЛЕВИЙ"):
    x="".join(x)
    if x[0]!='Й' and "ЕИ" not in x:
        cnt+=1
        print (x,cnt)

# 13:43