from time import *
ts=time()
with open("37359.txt") as f:
    # a=[int(x) for x in f]
    d=[[] for i in range(117)]
    cnt=0
    suma=-10**19
    for x in f:
        d[int(x)%117].append(int(x))

    for i in range(0,117):
        j=(117-i)%117
        if i==j:
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