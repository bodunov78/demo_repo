#20:57
from turtle import *
tracer(0)
screensize(5000,5000)
k=20
down()
# speed(5)
for x in range(2):
    fd(16*k)
    rt(90)
    fd(22*k)
    rt(90)
up()
fd(5*k)
rt(90)
fd(5*k)
lt(90)
down()
for x in range(2):
    fd(52*k)
    rt(90)
    fd(77*k)
    rt(90)

up()

for x in range(-10,50):
    for y in range(-50,10):
        # color("Red")
        goto(x*k,y*k)
        dot(4,"red")

# update()
done()
# 21:32
#