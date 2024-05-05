from  turtle import *


# --- functions --- (lower_case_names)

def get_pixel_color(x, y):
    # canvas use different coordinates than turtle
    y = -y

    # get access to tkinter.Canvas
    canvas = getcanvas()

    # find IDs of all objects in rectangle (x, y, x, y)
    ids = canvas.find_overlapping(x, y, x, y)

    # if found objects
    if ids:
        # get ID of last object (top most)
        index = ids[-1]

        # get its color
        color = canvas.itemcget(index, "fill")

        # if it has color then return it
        if color:
            return color

    # if there was no object then return "white" - background color in turtle
    return "white"  # default color


# def draw_rect(x1, y1, width, height, color):
#     # canvas use different coordinates than turtle
#     y1 = -y1
#     # get access to tkinter.Canvas
#     canvas = turtle.getcanvas()
#     # draw using tkinter.Canvas
#     canvas.create_rectangle((x1, y1, x1 + width, y1 + height), fill=color, width=0)
#
#
# def on_mouse_click(x, y):
#     print('Color:', get_pixel_color(x, y))
#

# --- main ---

# draw red square
#
# turtle.up()
# turtle.goto(0, 0)
# turtle.down()
#
# turtle.color("red")
#
# turtle.begin_fill()
#
# for _ in range(4):
#     turtle.forward(50)
#     turtle.right(90)
#
# turtle.end_fill()
#
# # draw green square
#
# turtle.up()
# turtle.goto(100, 100)
# turtle.down()
#
# turtle.color("green")
#
# turtle.begin_fill()
#
# for _ in range(4):
#     turtle.forward(50)
#     turtle.right(90)
#
# turtle.end_fill()
#
# # use tkinter.Canvas to draw rectangle
#
# draw_rect(100, -100, 200, 50, "blue")
#
# # run function on mouse click
#
# turtle.onscreenclick(on_mouse_click)
#
# # start "the engine" - mainloop
#
# # turtle.done()
# turtle.mainloop()
screen=Screen()
left(90)
speed(10000)
color('black','red');
# screen.bgcolor("orange")
k = 20
x = 4
begin_fill()
down()
# for i in range(4):
#     forward(x * k)
#     right(90)
#     forward(x * k)
#     left(90)
#     forward(x * k)
#     right(90)
for i in range(10):
    forward(5*k)
    right(60)




up()
end_fill()
cnt=0
hideturtle()
for i in range(0, 3 * x + 1):
    for y in range(-x, 2 * x + 1):
        goto(i * k, y * k)
        print(get_pixel_color(i * k, y * k))

        if get_pixel_color(i * k, y * k) =="red":
            cnt+=1
            dot(4,"white")
        else:
            dot(4, "green")
        # begin_fill()
        # print(color())
        # sc = t.getcanvas()
        # h=sc.find_overlapping(i*k,y*k,i*k,y*k)
        # print (k)
#
# k = 20
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
print(cnt)
done()