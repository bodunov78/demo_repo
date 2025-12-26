from turtle import *
k=40

speed(120)
up()
for x in range(-10*k,10*k,k):
    for y in range(-10 * k, 10 * k, k):
        goto(x,y)
        dot(5,"red")

goto(0,0)
down()

for i in range(10):
    forward(5*k)
    right(60)
done()
#
# for x in range(-10*k,10*k,k):
#     for y in range(-10 * k, 10 * k, k):
#         goto(x,y)
#         dot(5,"red")



