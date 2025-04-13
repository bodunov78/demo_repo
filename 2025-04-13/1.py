from re import *
with open("24_17641.txt") as f:

    s=f.readline()
    print (len(s))
    s=s.replace('**'," ").replace('++'," ").replace('+*'," ").replace('*+'," ")

    s=s.strip()

    m=0
    k=[]
    for x in s.split():
        # print(x)
        if len(x)>m:
            for i in range(len(x)-1):
                if x[i] not in "+*":
                    sub=""
                    for j in range(i+1,len(x)):
                        sub+=x[j]
                        try:
                            if x[j] not in "+*"  and eval(x[i:j])==0:
                                # print(i,j,x[i:j],x)
                                k.append(len(sub))
                                m=max(m,len(sub))
                        except:
                            pass
    print(max(k))






    # num=r'[1-9][0-9]*|0'
    # proiz=rf'(({num}\*)*0(\*{num})*)'
    # reg=rf'{proiz}([+*]{proiz})+'
    # m=[len(x.group()) for x in finditer(reg,s)]
    # # k=[]
    # # for x in m:
    # #     if eval(x)==0:
    # #         k.append(len(x))
    # print (max(m))