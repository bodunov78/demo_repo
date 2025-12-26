with open("test_1.csv", encoding="utf8") as f:
    s=f.readline()
    cnt=1
    for s in f:
        s=s.strip().replace('\xa0', ' ')
        cnt+=1
        m=s.split(';')
        # print (cnt,len(m),m)

        q1=f"{m[2]}\n{m[3]}"
        a1 = m[4]
        a2 = m[5]
        a3 = m[6]
        a4 = m[7]
        a5 = m[8]
        print (f"{q1}\n,{a1},{a2},{a3},{a4},{a5}")
        if cnt == 21:
            break