def fufu(x,A):
    return (((x&29)!=0) <= (((x&17)==0) <=((x&A)!=0)))

def fufu2(x,A):
    return (((x&29)==0) or (((x&17)!=0) or ((x&A)!=0)))

for A in range(0,100):
    if all([fufu2(x,A) for x in range(0,1000)]):
        print (A)


a=[0,0,0,0,False]
print (all(a))
print (any(a))
