with open("58535B.txt") as f :
    n=f.readline()
    a=[int(x) for x in f]
    b=[[[] for j in range(7)] for i in range(7)]

    for i,v in enumerate(a):
        b[i%7][v%7].append(v)

    print (b)