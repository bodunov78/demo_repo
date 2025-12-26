
arr=[(10, 10),(10, 6),(-4, 8),(2, 9),(12, 7),(-11, 4),(-8, 13), (10, 9),(11, 11)]
for x in arr:
    s=x[0]
    t=x[1]
    print (s,t)
    if s > 10 and t > 10:
        print("YES")
    else:
        print("NO")

    # print (s,t)