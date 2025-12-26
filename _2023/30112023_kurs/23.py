def f(x,y,n):
    if x>y:
        # print (x,y,n,"x>y")
        return 0
    elif x==10:
        return 0
    elif(x == y):
        # print (x,y,n,"x==y")
        return 1
    else : return f(x+1,y,n+1)+f(x+3,y,n+1)+f(x*2,y,n+1)

print(f(2,7,0)*( f(7,15,0)-f(7,10,0)*f(10,15,0) ) )

# print(f(2,7,0)*( f(7,15,0) ))

