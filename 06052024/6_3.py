from  turtle import *
new_turtle=Turtle()

# --- functions --- (lower_case_names)

def get_pixel_color(x, y):
    # canvas use different coordinates than turtle
    y = -y

    # get access to tkinter.Canvas
    canvas = getcanvas()

    # find IDs of all objects in rectangle (x, y, x, y)
    ids = canvas.find_overlapping(x, y, x, y)

    # if found objects
    print (ids)
    if ids:
        # get ID of last object (top most)
        index = ids[-1]

        # get its color
        color = canvas.itemcget(index, "fill")

        # if it has color then return it
        if color:
            return (color)

    # if there was no object then return "white" - background color in turtle
    return ("white")  # default color


k=10
speed(10000)
color("black","green")
fillcolor("black")
# bgcolor("orange")
#hideturtle()


# begin_fill()
up()
for x in range(0,20*k,k):
    for y in range(0,20*k,k):
        goto(x,y)
        dot(4, "red")

goto(100,100)


# bgcolor("red")
# bgcolor("white")


for i in range(1):
    begin_fill()
    # print (xcor(),ycor())
    for i in range(10):
        forward(5*k)
        right(60)
    end_fill()

hideturtle()
# goto(200,200)

black=0
green=0



for x in range(0*k,20*k,k):
    for y in range(0*k,20*k,k):
        goto(x,y)
        print (xcor(),ycor(),get_pixel_color(x,y))
        if get_pixel_color(float(x),float(y))=="black":
            black+=1
            dot(4, "white")
        elif get_pixel_color(x,y)=="red":
            green+=1
        else:
            dot(4,"red")


print(black,green,black+green)
done()
# exitonclick()








        # begin_fill()
        # print(color())
        # sc = t.getcanvas()
        # h=sc.find_overlapping(i*k,y*k,i*k,y*k)
        # print (k)



#
# k = 40
# x = 4
# goto(0,0)
# begin_fill()
# down()
# for i in range(4):
#     forward(x * k)
#     right(90)
#     forward(x * k)
#     left(90)
#     forward(x * k)
#     right(90)
# up()
# end_fill()
# goto(0,0)
# hideturtle()
# x=4
# for i in range(0, 3 * x + 1):
#     for y in range(-x, 2 * x + 1):
#         goto(i * k, y * k)
#         xx,yy=i * k, y * k
#         print(get_pixel_color(xx,yy))
#         begin_fill()
#         # print(color())
#         # sc = t.getcanvas()
#         # h=sc.find_overlapping(i*k,y*k,i*k,y*k)
#         print (k)
#
#
# # screen.onclick(dot(4,"blue"))
# print(cnt)
# done()