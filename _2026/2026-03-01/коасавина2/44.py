def f(ch,ss):
    res=""
    while ch>0:
        res=str(ch%ss)+res
        ch=ch//ss
    return res

print(f(123456,30))
