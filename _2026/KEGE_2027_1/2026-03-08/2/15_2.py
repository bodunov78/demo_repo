#15928
def fufu(x,y,a1,a2):
    return (( a1<=x<=a2) <= (((x*x)<=81))) and   (  ((y*y)<=36) <=  (   a1<=y<=a2  )    )

arr=[]
for a1 in range(-30,30):
    for a2 in range(a1+1,30):
        if all([fufu(x,y,a1,a2) for x in range(-13,13) for y in range(-13,13)]):
            arr.append((a2-a1,a1,a2))
print (max(arr))

