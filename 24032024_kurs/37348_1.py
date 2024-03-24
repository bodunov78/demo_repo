from time import *
ts=time()
with open("37348.txt") as f:

# не верно

    # a=[int(x) for x in f]
    d=[[] for i in range(117)]
    cnt=0
    suma=-10**19
    for x in f:
        d[int(x)%34].append(int(x))

    for i in range(34):
        d[i].sort()

    for i in range(1,34):
        for i in(1,34)

        if (i+j)%34!=0:
            d[i].sort()
            maxi = d[i][-1] + d[i][-2]
            print(maxi, len(d[i]))
            suma = max(suma, maxi)
            cnt = cnt + len(d[i]) * (len(d[i]) - 1) / 2
            print(maxi, i, len(d[i]), len(d[j]), cnt)

        elif i<j:
            maxi=max(d[i])+max(d[j])
            # print(maxi,i,len(d[i]),len(d[j]))
            suma=max(suma,maxi)
            cnt=cnt+len(d[i])*len(d[j])
            print(maxi, i, len(d[i]), len(d[j]),cnt)

    print(cnt,suma)
print(time()-ts)