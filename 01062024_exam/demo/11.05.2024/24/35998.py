with open("35998.txt") as f :
    m=[]
    for s in f:
        s=s.strip()

        if s.count('A')<25:
            for c in set(s):
                if s.count(c)>1:
                    m.append((s.rindex(c)-s.index(c),c )    )

            print(m)

    print (max(m))