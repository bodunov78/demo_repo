f=open("27_B.txt")
n=int(f.readline())
suma=0
mina=10**20

ost=[10**20]*19

for i in range(n):
    s=f.readline()
    a=list(map(int,s.split()))
    #print (a)
    mina=(max(a)-min(a))

    if mina !=0 :
        ost[mina%19]=min(ost[mina%19],mina)
        #print (mina,mina%19)
    suma=suma+max(a)
    #print(suma,mina, mina % 19)


print (ost)
print(suma,ost[suma%19])


if suma%19 !=0:
    print("!0",suma-ost[suma%19])
else:
    print("0",suma)
print(suma,suma%19)
