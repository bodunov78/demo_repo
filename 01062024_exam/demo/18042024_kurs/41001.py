import operator
from time import *
ts=time()
with open("41001.txt") as f:
    N=int(f.readline())
    t=[list(map(int,x.split())) for x in f]
    t.sort()
    print (t)
    m=[]
    ss=1634515200
    ee=ss+7*24*60*60
    for x in t:
        if x[1]<ss or x[0]>ee:
            continue
        else:
            if x[0]<ss:
                x[0]=ss
            if x[1] > ee:
                x[1] = ee
            m.append(x)


    print (len(t),m)

    wend=[0]*7*24*60*60
    for (s,e) in m:
        a=[0]*(s-ss)+[1]*(e-s) +[0]*(len(wend)-(e-ss))
        # print (len(a))
        wend = list(map(operator.add, wend, a))
        # print(result)

    print (len(wend))

print (time()-ts)