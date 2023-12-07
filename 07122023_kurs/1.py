def fufu(cmd,s,e,b):
    print (cmd,s,e,b)
    for c in cmd:
        if c=='1':
            s=s+2
        elif c=='2'and (s/b == int(s/b)):
            s=s/b
    if s ==e :
        return (b)
    else:
        return(0)

for x in range(1,100):
    z=fufu('11211',50,22,x)
    print (z)
