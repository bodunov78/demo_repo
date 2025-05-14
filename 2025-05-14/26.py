#12:11

with open("26_19256.txt") as f:
    n=f.readline()
    m=[tuple(map(int,x.split())) for x in f]
    a=list(set(m))
    a.sort()
    # for x in m :
    #     a+=[]
    print(a[:10])
    k=1
    n=[]
    for i in range(len(a)-1):
        if a[i][0]==a[i+1][0] and a[i+1][1]-a[i][1]==1:
            k+=1

        else:
            n.append([k,a[i][0]])
            k=1
    n.sort(reverse=1)
    for x in n:
        if x[0]==148:
            print (x)
    print (max(n),n[0])
#12:27

