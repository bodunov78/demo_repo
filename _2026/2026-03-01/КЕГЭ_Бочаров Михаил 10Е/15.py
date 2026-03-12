def r(x,y,z):
    a=[]
    k=x
    while k<y:
        a.append(float(k))
        k=k+z
    return(a)
print(r(1,10,1))
