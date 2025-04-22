def f(n):
    if n==1: return 0
    else: return (f(n-1)+n)

def g(n):
    if n==1: return 1
    else: return (g(n-1)*n)


print (f(5)+g(5))
#14:25
