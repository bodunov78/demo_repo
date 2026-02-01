with open("5900.txt",encoding="utf-8") as f:
    a=[]
    b=[]
    for s in f:
        s=s.replace('.',' ').replace(',',' ').replace('!',' ').replace('?',' ').replace(':',' ').replace(';',' ').replace('\"',' ').replace('\'',' ').upper().replace('-',' ').strip()
        m=s.split()
        # print (m)
        ss="АЕЁИОУЫЭЮЯ"

        for x in m:
            a.append(x)

            # if len(x)>1 and x not in ss:
            #
            # if ('в' in x) and ('о' not in x) and ('а' not in x):
            #     a.append(x)

    print (len(a))

    for c in ss:
        while c in a:
            a.remove(c)
    suma=0
    for x in a:
        for c in ss:
            x=x.replace(c,'@')
        suma+=x.count('@')


    print (suma)



