from turtle import *

screensize(5000,5000)
tracer(0)
down()
k=20
for i in range(8):
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

for i in range(8):
    fd(52*k)
    rt(90)
    fd(77*k)
    rt(90)

up()

for i in range (-50,50):
    for j in range(-50,50):
        goto(i*k,j*k)
        dot(3,"Red")

done()