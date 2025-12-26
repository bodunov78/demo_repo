from turtle import *


k=40
speed(50)
begin_poly()
print(position())
for i in range(10):

    fd(5*k)
    rt(60)
    print(position())

end_poly()
print(get_poly())
up()


for x in range(-10*k,10*k,k):
    for y in range(-10*k,10*k,k):
        goto(x,y)
        dot(3,"red")

done()
