f=open("17_37361.txt")

a=[int(x) for x in f]
cnt=0
sums=0
for i in range(len(a)-1):
    for j in range(i+1,len(a)):
        suma=a[i]+a[j]
        if suma%126==0:
            cnt+=1
            sums=max(sums,suma)
            print(cnt,sums)





