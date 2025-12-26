for i in range(100,200):
    s=list(str(i).split('2'))
    print(s)
    s="222222"
    print(s.rjust(5,"*"))
    print(s.ljust(5, "*"))
    print(s.strip().rjust(10,'#'))
    print (s.replace('22','2:2'))
    hehex="0123456789ABCDEF"
    for i in range(0,257):
        ost=i
        s=""
        while ost>0:
            s=str(hehex[ost%16])+s
            ost//=16
        print(s)
        for i in range(10,20):
            for j in range(20,30):
                k=f'{i}-{j}'
                print(k)
