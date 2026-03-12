def range(start,stop,step):
    res=[]
    if step>0:
        while start < stop:
            res.append(round(start,5))
            start+=step
    elif step<0:
        while start>stop:
            res.append(round(start,5))
            start+=step
    return res
a,b,c = map(float,input().split())

print(range(a,b,c))  