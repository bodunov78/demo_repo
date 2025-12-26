from turtle import *

color("red")
k = 20
speed(0)
hideturtle()

pd()
begin_fill()
for i in range(6):
    forward(10 * k)
    right(60)
end_fill()

c = 0
canvas = getcanvas()
penup();
tracer(0)
for x in range(-20 * k, 20 * k, k):
    for y in range(-20 * k, 20 * k, k):
        if canvas.find_overlapping(x, y, x, y):
            c += 1
            goto(x, -y);
            dot(5, 'blue')
        else:
            goto(x, -y);
            dot(3, 'gray')

print(c)
done()