
for a in range(100):
    flag=1
    for x in range(1000):
        for y in range(1000):
            if (not ((x+2*y<a) or (y>x) or (x>20))):
                flag=0
    if flag==1:
        print (a)

