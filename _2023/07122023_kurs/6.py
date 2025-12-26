from itertools import *
def kucha(m,sm):
    flag=1
    for y in m:
        suma=sm
        for x in y:
            if x =='1':
                suma=suma+1
            elif x=='4':
                suma=suma+4
            else:
                suma=suma*5
        if suma<68:
            flag=0
        # return 0
    if flag==1:
        print(sm)




# s="145"
# m=[list(x)+list(y) for x in product(s,repeat=3) for y in product('AB',repeat=3) ]
# print(m)

# for suma in range(1,68):
#     kucha(m,suma)

k=('1','2','3','4','5')
l=('3','4')
# print("Fuck",)

if "".join(l) in "".join(k):
    print("\nOk")
else:
    print("Fuck",l,k)
