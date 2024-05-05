# from turtle import *
# k = 5;
# speed(0);
# color('black','red');
# hideturtle();
# begin_fill()
# for i in range(5):
#    seth(0);
#    circle(5*k, 180);
#    seth(90);
#    circle(5*k, 180);
#    seth(180);
#    circle(5*k, 180);
#    seth(270);
#    circle(5*k, 180)
# end_fill(); sc = getcanvas()
# otv = ['in' if (h:=sc.find_overlapping(x,y,x,y)) and sc.itemcget(h[-1], 'fill')=='red' else 0
#        for x in range(-100*k,100*k,k) for y in range(-100*k,100*k,k)]
# print(otv.count('in'))


from turtle import  *
screen=Screen()
left(90)
speed(1000)
color('black','red');
# screen.bgcolor("orange")
k = 20
x = 2




down()
for i in range(4):
    forward(x * k)
    right(90)
    forward(x * k)
    left(90)
    forward(x * k)
    right(90)
up()
for i in range(0, 3 * x + 1):
    for y in range(-x, 2 * x + 1):
        goto(i * k, y * k)
        dot(2,"green")
        begin_fill()
        print(color())
        # sc = t.getcanvas()
        # h=sc.find_overlapping(i*k,y*k,i*k,y*k)
        print (k)


# screen.onclick(dot(4,"blue"))
done()
