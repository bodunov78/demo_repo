def f():
    p=5
    q=7

    return (p-1)*(q-1)

e=11
for d in range(40):
    if (d*e)%f()==1:
        print (d)