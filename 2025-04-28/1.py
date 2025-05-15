# 20:28
from itertools import *
tab="12,13,14,25,27,34,37,48,56,58,68"
gr="AG,AF,GF,DG,HF,EH,CH,CB,BE,BD,DE"
tab=tab+','+tab[::-1]
gr=gr+','+gr[::-1]
s=list(set(list(gr.replace(',',''))))
print (s)
for x in permutations(s):
    ntab=gr
    for i,v in enumerate(x):
        ntab=ntab.replace(v,str(i+1))
    if set(tab.split(','))==set(ntab.split(',')):
        print(x)

        # 20:34
        