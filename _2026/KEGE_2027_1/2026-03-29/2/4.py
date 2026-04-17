from pickle import *
with open("b.txt") as f , open("Big_array.bin","wb") as ba:
    b=[]
    for s in f:
        m=[float(x) for x in s.split()]
        b.append(m)
    print (len(b),b[:3])
    dump(b,ba)
