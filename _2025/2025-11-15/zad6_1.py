import math


a=[(x,y) for x in range(0,113+1) for y in range(0,140+1)]


def distance(x1, y1, x2, y2):
    """Рассчёт евклидова расстояния между двумя точками."""
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)


def on_segment(x1, y1, x2, y2, xc, yc):
    """
    Проверяет, лежит ли точка C(xc,yc) на отрезке A(x1,y1)-B(x2,y2).
    Возвращает True, если да, иначе False.
    """
    L_AB = distance(x1, y1, x2, y2)
    L_CA = distance(x1, y1, xc, yc)
    L_CB = distance(x2, y2, xc, yc)

    # Условие принадлежности: сумма CA и CB должна быть равна AB
    return math.isclose(L_CA + L_CB, L_AB, rel_tol=1e-9)


# Тестирование
x1, y1 = 0, 0
x2, y2 = 100, 102
xc, yc = 100, 100

if on_segment(x1, y1, x2, y2, xc, yc):
    print("Точка лежит на отрезке.")
else:
    print("Точка не лежит на отрезке.")


a=[(x,y) for x in range(x1,x2+1) for y in range(y1,y2+1)]

for xc,yc in a:
    if on_segment(x1, y1, x2, y2, xc, yc):
        print((xc,yc),"Точка лежит на отрезке.")
    # else:
    #     print("Точка не лежит на отрезке.")

