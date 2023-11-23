i=1024*27*125*49*6*18

d=dict()
j=2
while j<=i:
    if i %j ==0:

        d[j]=d.get(j,0)+1
        i=i//j
    else:
        j+=1
    print(i,j)
print(d)

