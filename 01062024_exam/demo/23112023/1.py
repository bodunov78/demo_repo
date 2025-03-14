def fact(n):
    if n>0:
        print (n)
        return n*fact(n-1)
    else:
        return 1

print(fact(4))

