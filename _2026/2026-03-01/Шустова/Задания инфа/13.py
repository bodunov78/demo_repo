
def f(a, b):
    x=a
    y=b
    while y:
        x, y = y, x%y
   
    if x!=0:
        z=(a * b) // x
    else:
        z=0
    return x, z

print(f(12, 16))
