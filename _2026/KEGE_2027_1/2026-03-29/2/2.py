
with open("b.txt") as f , open("c.txt","w") as fw:
    for s in f:
        m=[int(float(x)) for x in s.split()]
        print (*m,file=fw)
