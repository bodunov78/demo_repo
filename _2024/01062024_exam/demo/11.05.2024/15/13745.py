def fu(x,y,a):
    return ((x <= 9) <= (x * x <= a)) and ((y*y <= a) <= (y <= 9))

for a in range(1, 300):
    k = 0
    if all(fu(x,y,a) for x in range(0,300) for y in range(300)):
        print(a)
