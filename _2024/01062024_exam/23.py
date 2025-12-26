#18724
def f(x, y):
    if x > y:
        return 0
    if x == y:
        return 1
    else:
        return f(x + 1, y) + f(x * 3, y) + f(x + 2, y)
print(f(1, 10) * f(10, 12) * f(12, 15))

#15932

def f(x, y):
    if x > y or x == 29:
        return 0
    if x == y:
        return 1
    else:
        return f(x + 1, y) + f(x * 2, y) + f(x * 3, y)
print(f(2, 13) * f(13, 44))