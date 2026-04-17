with open("26_23283_2.txt",encoding="utf-8") as f:
    K=int(f.readline())
    N=int(f.readline())
    a=[]
    for s in f:
        st,end =[int(x) for x in s.split()]
        a.append([st,end])

    a.sort()
    okna=[0]*(K+1)
    count=0
    last=0

    for st,end in a:
        for j in range(1,K+1):
            if okna[j] <st:
                okna[j] = end
                count+=1
                last = j
                break
    print (count,last)