from turtle import *
visited_points = set()  # Набор уникальных точек

def record_position():
    """Регистрирует текущее положение черепахи"""
    current_pos = tuple(map(float, position()))  # округляем координаты до целых чисел
    print (current_pos)
    visited_points.add(current_pos)

# def ff():
#     t = turtle.Turtle()
#     t.speed(1)
#
#     # Новая логика регистрации позиций
#     record_position()  # добавляем первую точку старта
#
#     # Движение черепахи
#     t.forward(100); record_position()
#     t.left(90);       record_position()
#     t.forward(100);  record_position()
#     t.left(90);       record_position()
#     t.forward(100);  record_position()
#     t.left(90);       record_position()
#     t.forward(100);  record_position()
#
#     # Показываем количество уникальных точек
#     print("Количество уникальных точек:", len(visited_points))
#
#     turtle.done()

def find_coordinates(x1, y1, x2, y2, epsilon=1e-0):
    def almost_equal(a, b):
        return abs(a - b) < epsilon

    dx = abs(x2 - x1)
    dy = abs(y2 - y1)
    sx = 1 if x1 < x2 else -1
    sy = 1 if y1 < y2 else -1
    err = dx - dy

    coordinates = []
    while True:
        # if int(x1)%20==0 and int(y1)%20==0:
        coordinates.append((round(x1, 3), round(y1, 3)))  # Округление до 3 знаков после запятой

        if almost_equal(x1, x2) and almost_equal(y1, y2):
            break
        e2 = 2 * err
        if e2 > -dy:
            err -= dy
            x1 += sx
        if e2 < dx:
            err += dx
            y1 += sy

    return coordinates



def f5():


    screensize(5000, 5000)
    tracer(0)
    down()
    k = 20
    record_position()
    for i in range(2):
        fd(27 * k); record_position()
        rt(90)
        fd(8 * k)
        rt(90)
    up()

    fd(4 * k)
    rt(90)
    fd(2 * k)
    lt(90)
    down()

    for i in range(2):
        fd(17 * k)
        rt(90)
        fd(7 * k)
        rt(90)

    up()

    for i in range(-50, 50):
        for j in range(-50, 50):
            goto(i * k, j * k)
            dot(3, "Red")

    done()

f5()
print("Количество уникальных точек:", len(visited_points))

for x,y in find_coordinates(0,0,140,113):
    print (x,y)
# print (find_coordinates(0,0,100,100))