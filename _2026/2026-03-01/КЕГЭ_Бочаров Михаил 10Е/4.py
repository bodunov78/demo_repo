def f(x,n):
    a=''
    while x>0:
        a=str(x%n)+a
    return a
print(f(123456,30))
