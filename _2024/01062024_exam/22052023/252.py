maxa=0
for i in range(84052,84130+1):
    a=[]
    for j in range(1,i+1):
        if i%j==0:
            a.append(j)
            #print (a)
    maxa=max(maxa,len(a))
    print(i,maxa)

