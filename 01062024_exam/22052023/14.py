for i in range(15):
    d=5+i*15+3*15**2+2*15**3+1*15**4+3+3*15+2*15**2+i*15**3+1*15**4
    if d%14==0:
        print(i,d/14)