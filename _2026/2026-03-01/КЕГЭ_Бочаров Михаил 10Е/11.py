def f(x):
    a=''
    for k in range(1,x+1):
        if x%k==0:
            a=a+str(k)+', '
    return(a)

for i in range(1001,2001):
    print(i,':',f(i))
