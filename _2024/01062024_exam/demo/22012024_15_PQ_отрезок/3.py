#Тип 15 8666
#Тип 15 11119









def frr(a,b,c):
    x=a
    m=[]
    while x<b:
        m.append(x)
        x+=c

    return m


P=[x for x in frr(20,50+0.5,0.5)]
Q=[x for x in frr(30,65+0.5,0.5)]
A=[x for x in frr(0,1000+0.5,0.5)]
d=[]


list = []
for Amin in frr(1, 100,0.5):
    for Amax in frr(Amin + 0.5, 100,0.5):
        check = 1
        A = [i for i in frr(Amin, Amax,0.5)]
        for x in frr(-150, 100,0.5):
            f = (not(x in A)) <= (((x in P) and (x in Q)) <= (x in A))
            if not f:
                check = 0
                break
        if check == 1:
            m = Amax - Amin
            list.append(m)
print(min(list)-1)
