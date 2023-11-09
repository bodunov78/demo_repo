i=123
d=dict()
j=2
while j<=i:
    if i %j ==0:
        if d.get(j,0)==0:
            d[j]=1
        else:
            d[j]+=1
        i=i//j
    else:
        j+=1

    print(i,j)
print(d)