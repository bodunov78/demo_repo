with open("27423.txt") as f:
    a,b=map(int,f.readline().split())
    print (a,b)
    arr=[int(x) for x in f]
    arr.sort()
    print (len(arr),arr[-1])
    m=list(set(arr))
    print (m)
    for i in range(len(arr)):
        if sum(arr[:i]) <= a:
            sumax=sum(arr[:i])
            sumi=i-1
            print (i,sum(arr[:i]))
        else:
            print(arr[i],sum(arr[:sumi])+arr[i])