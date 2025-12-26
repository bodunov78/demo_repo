def fufu(n,m):
    if n>m:
        print(n)
        return fufu(n-1,m)
    else:
        return 0


a=fufu(6,1)
print (a)



