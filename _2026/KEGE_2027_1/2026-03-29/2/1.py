suma=0
lena=0
with open("b.txt") as f:
    for s in f:
        m=[float(x) for x in s.split()]
        suma+=sum(m)
        lena+=len(m)
        print (sum(m)/len(m))
print ("file:",suma/lena)