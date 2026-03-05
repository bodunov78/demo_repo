def fac(a):
    if a<=1:
        return 1
    else:
        return a*fac(a-1)
b=int(input())
print(fac(6b))