stat=[(0,'L','L','R',1),(1,'L','L','S',1),(1,2,0,'R',1),(1,1,2,'R',1),(1,0,1,'R',1)]
s='R'
q=0
ss=list('L1021010201001L')
print (ss)
q=0
for i,v in enumerate(ss):
    # print (v)
    for st in stat:
        # print (st)
        if st[0]==q  and st[1]==v:

            ss[i]=st[2]
            q=st[4]
            s=st[3]
            print(i,q, ss, st)
            break
    if s=='S':
        break
print (ss)