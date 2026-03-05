f=open('test.txt','w')
for i in range(1001,2001):
    s=[]
    for j in range(1,i+1):
        if i%j==0:
            s.append(j)
    f.write(str(i)+': '+', '.join(map(str,s))+'\n')
f.close()
