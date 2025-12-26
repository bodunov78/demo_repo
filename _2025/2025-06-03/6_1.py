from turtle import *

screensize(5000,5000)
tracer(0)
k=20
down()
for i in range(9):
    fd(22*k)
    rt(90)
    fd(6*k)
    rt(90)

up()

fd(1 * k)
rt(90)
fd(5 * k)
lt(90)

down()
for i in range(9):
    fd(53*k)
    rt(90)
    fd(75*k)
    rt(90)
up()

for x in range(-30,300):
    for y in range(-30,30):
        goto(x*k,y*k)
        dot(3,"red")


done()



