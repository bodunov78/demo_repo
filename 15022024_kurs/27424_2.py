f=open("27-B_demo (1).txt")
n=int(f.readline())
suma=0
mina=10**19
for x in f:
    x=list(map(int,x.split()))
    if (max(x)-min(x))%3!=0:
        print(mina)

        mina=min(mina,max(x)-min(x))
    suma+=max(x)


if suma%3==0:
    suma-=mina

print (suma)