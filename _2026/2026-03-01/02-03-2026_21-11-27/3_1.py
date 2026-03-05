def f(n):
    s = ''
    while n!=0:
        s = str(n % 2) + s
        n = n // 2
    return s
print(f(127))
