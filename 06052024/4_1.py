
a=[]
def f(n):
    s = str(n)
    if len(s) == 5:
        a.append(s)
        return 1
    podr = []
    for i in range(10):
        if  i > int(s[-1]) and i%2 != int(s[-1])%2:
            podr.append(int(s+str(i)))

    print(podr)
    return sum(f(i) for i in podr)

print(sum(f(i) for i in range(1,10)))
print (a)