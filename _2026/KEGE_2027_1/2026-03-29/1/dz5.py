m=set()
for a in range(1,20):
    for b in range(a+1,20):
        for c in range(b+1,20):
            if a**2+b**2==c**2:
                m.add((a,b,c))
print (m)