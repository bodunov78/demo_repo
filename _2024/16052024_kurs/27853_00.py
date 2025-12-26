def de(x):
    a=set()
    for i in range(1,int(x**0.5)+1):
        if x%i==0:
            a.add(i)
            a.add(x//i)
    a=list(a)
    a.sort()
    return a



# print (len(de(12)))

for i in range(312614,312651+1):
    if len(de(i))==6:
        print (de(i))


