import math


def normalize_vector(vector):
    """Нормализует вектор."""
    magnitude = math.hypot(*vector)
    return tuple(coord / magnitude for coord in vector)


def vectors_are_parallel(v1, v2, v3):
    """Проверяет, параллельны ли векторы."""
    normalized_v1 = normalize_vector(v1)
    normalized_v2 = normalize_vector(v2)
    normalized_v2 = normalize_vector(v2)

    dot_product = sum(a * b for a, b in zip(normalized_v1, normalized_v2))

    return math.isclose(abs(dot_product), 1, abs_tol=1e-9)


def is_point_on_segment(x1, y1, x2, y2, xc, yc):
    """Проверяет, лежит ли точка C на отрезке AB."""
    # Формируем векторы
    ab = (x2 - x1, y2 - y1)
    ac = (xc - x1, yc - y1)
    cb = (x2 - xc, y2 - yc)
    # Проверяем параллельность векторов

    if not (xc == x1 and yc == y1) and not (xc == x2 and yc == y2) and not vectors_are_parallel(ab, ac):
        return False

    # Проверяем, что AC не превышает AB
    ab_magnitude = math.hypot(*ab)
    ac_magnitude = math.hypot(*ac)
    return ac_magnitude <= ab_magnitude


# Пример использования
x1, y1 = 0, 0
x2, y2 = 120, 651
xc, yc = 11, 140

on_segment = is_point_on_segment(x1, y1, x2, y2, xc, yc)
print(on_segment)
#
a = [(x, y) for x in range(x1, x2 + 1) for y in range(y1, y2 + 1)]

for xc, yc in a:
    if is_point_on_segment(x1, y1, x2, y2, xc, yc):
        print((xc, yc), "Точка лежит на отрезке.")
