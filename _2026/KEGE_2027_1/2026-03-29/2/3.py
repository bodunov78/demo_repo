
with open("b.txt") as f , open("int.txt","w") as fi, open("float.txt","w") as ff:
    for s in f:
        inta=[int(x) for x in s.split() if '.' not in x and 'e' not in x]
        floata = [float(x) for x in s.split() if '.'  in x or 'e' not in x]
        print(*inta,file=fi)
        print (*floata,file=ff)
        # print (*m,file=fw)
