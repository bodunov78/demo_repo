for N in range (100):
    bn=bin(N)[2:]
    if N%2==0:
        bn=bn+"10"
    else:
        bn="1"+bn+'00'
    R=int(bn,2)
    if R>107:
        print (N,R)