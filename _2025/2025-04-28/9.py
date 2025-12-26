# 0:37
with open("9.txt") as f:
    cnt=0
    for x in f:
        cnt+=1
        d=dict()
        a=list(map(int,x.split()))
        d=[a.count(x) for x in set(a)]
        d.sort()
        suma=0
        sumi=0
        if d==[1,3,3]:
            for i in set(a):
                if a.count(i)==3:
                    suma+=i
                else:
                    sumi=i
            suma=suma/2
            if suma<sumi:
                print(cnt)
#0:47
