with open("40742.txt") as f:
    n=int(f.readline())
    a=1633046400
    for x in f:
        sp,ep=map(int,x.split())
        print (sp,ep,sp-a,ep-a)