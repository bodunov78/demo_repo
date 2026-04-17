def f1(a,b,c):
    print ((a+b)*c)

f1(4,2,3)

f1(c=5,a=4,b=6)


x=['a','b','c']
y=[4,6,5]
di=dict(zip(x,y))
print (di)
f1(**di)