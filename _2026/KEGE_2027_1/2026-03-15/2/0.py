def f(a,b,c):
    print (a,b,c)
a=['b','a','c']
b=[1,2,3]

c=dict(zip(a,b))
print (c)
f(**c)

# f(b=1,a=2,c=3)