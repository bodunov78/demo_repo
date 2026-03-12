a = [15, 24, 101, 55]
def f(a):
    for i in range(len(a)):
        n = a[i]
        s = sum(int(d) for d in str(n))
        a[i] = n % s
    return a

print(f(a))
    
