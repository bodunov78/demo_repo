def fb(b):
    res=2
    cmd="21121"
    for c in cmd:
        if c=='1':
            res-=b
        elif c=='2':
            res*=5
    return res


for x in range(1,100):
    res=fb(x)
    if res==17:
        print(x)