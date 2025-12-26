cnt=0
s=500000
while cnt<5:
    for x in range(18,s-1,10):
        if s%x==0:
            print(s,x)
            cnt+=1
            break
    s+=1


