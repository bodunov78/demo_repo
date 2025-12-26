#21:39
from turtle import *
tracer(0)
screensize(10000,10000)
r=20
down()
for i in range(8):
    fd(16*r)
    rt(90)
    fd(22*r)
    rt(90)
up()
fd(5*r)
rt(90)
fd(5*r)
lt(90)
down()
for i in range(8):
    fd(52*r)
    rt(90)
    fd(77*r)
    rt(90)
up()

for x in range(-20,20):
    for y in range(-20,20):
        goto(x*r,y*r)
        dot(3,"red")

done()
#21:42