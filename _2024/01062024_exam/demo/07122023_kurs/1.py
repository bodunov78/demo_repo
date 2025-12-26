def fufu(cmd,s,e,b):
    #print (cmd,s,e,b)
    for c in cmd:
        if c=='1':
            s=s+5
        elif c=='2'and (s*b == int(s*b)):
            s=s*b
    if s ==e :
        return (b)
    else:
        return(0)

for b in range(1,100):
    z=fufu('12111',6,48,b)
    if z:
        print (z)
