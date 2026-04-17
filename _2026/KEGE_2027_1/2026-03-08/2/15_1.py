#13745
def fufu(x,y,A):
    return ((x<=9) <=((x**2)<=A)) and (   ((y**2)<=A) <=(y<=9)         )

for A in range(-100,100):
    if all([fufu(x,y,A) for x in range(100) for y in range(100)]):
        print (A)
