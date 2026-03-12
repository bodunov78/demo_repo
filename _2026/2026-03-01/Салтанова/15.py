def f(start, end, step):
    s=[]
    while start<=end:
        s.append(start)
        start+=step
    return s
print(f(0,10,0.5))