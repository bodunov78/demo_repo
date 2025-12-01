import math


def line_equation_from_two_points(x1, y1, x2, y2):
    """Возвращает коэффициенты уравнения прямой Ax + By + C = 0."""
    A = y2 - y1
    B = x1 - x2
    C = x2 * y1 - x1 * y2
    return A, B, C


def distance_point_to_line(xc, yc, A, B, C):
    """Вычисляет расстояние от точки до прямой."""
    numerator = abs(A * xc + B * yc + C)
    denominator = math.sqrt(A * A + B * B)
    return numerator / denominator


def scalar_product(v1, v2):
    """Вычисляет скалярное произведение векторов."""
    return v1[0] * v2[0] + v1[1] * v2[1]


def is_point_between(x1, y1, x2, y2, xc, yc):
    """Проверяет, лежит ли точка C между точками A и B."""
    ac = (xc - x1, yc - y1)
    ab = (x2 - x1, y2 - y1)
    bc = (xc - x2, yc - y2)
    ba = (x1 - x2, y1 - y2)

    # Скалярные произведения должны быть положительными
    sp1 = scalar_product(ac, ab)
    sp2 = scalar_product(bc, ba)
    return sp1 >= 0 and sp2 >= 0


def is_point_on_segment(x1, y1, x2, y2, xc, yc):
    """Проверяет, лежит ли точка C на отрезке AB."""
    # Находим уравнение прямой
    A, B, C = line_equation_from_two_points(x1, y1, x2, y2)

    # Вычисляем расстояние от точки до прямой
    dist = distance_point_to_line(xc, yc, A, B, C)

    # Проверяем, что расстояние почти равно нулю
    if not math.isclose(dist, 0, abs_tol=1e-9):
        return False

    # Проверяем, что точка лежит между A и B
    return is_point_between(x1, y1, x2, y2, xc, yc)


# Пример использования
x1, y1 = 0, 0
x2, y2 = 113, 140
xc, yc = 101, 82

result = is_point_on_segment(x1, y1, x2, y2, xc, yc)
print(result)
a = [(x, y) for x in range(x1, x2 + 1) for y in range(y1, y2 + 1)]

for xc, yc in a:
    if is_point_on_segment(x1, y1, x2, y2, xc, yc)<1e-9:
        print((xc, yc), "Точка лежит на отрезке.")
#
#
#
# for xc, yc in a:
#     if is_point_on_segment(x1, y1, x2, y2, xc, yc):
#         print((xc, yc), "Точка лежит на отрезке.")
