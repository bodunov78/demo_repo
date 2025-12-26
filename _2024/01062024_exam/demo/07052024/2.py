arr=[(13,2), (11,12), (-12,12), (2,-2), (-10, -10), (6, -5), (2,8), (9,10), (1,13)]

for A in range(-10,100):
    cnt=0
    for s,t in arr:
        if s>A or t >12:
            k=1
            # print ("Yes")
        else:
            cnt+=1
            # print ("NO")
    if cnt==8:
        print (A)