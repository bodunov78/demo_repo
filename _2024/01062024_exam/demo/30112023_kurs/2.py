def fi(n):
    if n>10:
        return 0
    else:
        return n+fi(n+1)
print(fi(1))


