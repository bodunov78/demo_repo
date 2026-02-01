with open("10_4322.txt") as f:
    a=[]
    for s in f:
        s=s.replace('.',' ').replace(',',' ').replace('!',' ').replace('?',' ').replace(':',' ').replace(';',' ').lower().strip()
        m=s.split()
        for x in m:
            if ('в' in x) and ('о' not in x) and ('а' not in x):
                a.append(x)


    print ((len(a)))




