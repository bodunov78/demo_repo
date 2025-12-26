with open("10.txt") as f:
    for x in f:
        a=list(x.split())
        if 'долг' in a:
            print(a)