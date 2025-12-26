with open("47230.txt") as f:
    n=int(f.readline())
    a=[int(x) for x in f]

a.sort(reverse=1)

# x=a[0]
for j in range(0,10):
    x = a[j]
    b=[x]
    for i in range(j+1,len(a)):
        if x-a[i]>=3 :
            b.append(a[i])
            x=a[i]

    print(len(b),b[-1])


# print (a[0],a[-1])