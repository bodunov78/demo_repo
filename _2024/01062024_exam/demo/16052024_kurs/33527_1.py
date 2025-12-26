k=0
for i in range(101*10**6,102*10**6):
    cnt=0
    for j in range(2,int(i**0.5)+1,2):
        if i % j==0:
            cnt+=1
        if cnt>3:
            break
    if cnt==3:
        k+=1

print(k)