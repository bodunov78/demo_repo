def nod(a, b):
    while b:
        a, b = b, a % b
    return a
def nok(a,b):
    return (a*b)/nod(a,b)
a,b=map(int,input().split())
print(nod(a,b))
print(nok(a,b))