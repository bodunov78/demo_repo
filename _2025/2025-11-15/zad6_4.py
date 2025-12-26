from PIL import Image, ImageDraw
import math

def extract_red_pixels(image, color_threshold=10):
    """Выделяет точки с цветом, близким к указанному."""
    red = (255, 0, 0)  # Красный цвет
    pixels = image.load()
    width, height = image.size
    result = []

    for x in range(width//20):
        for y in range(height//20):
            r, g, b = pixels[x*20, y*20]

            # Проверяем близость к красному цвету
            if all(math.isclose(r, rc, abs_tol=color_threshold) for r, rc in zip(red, (r, g, b))):
                result.append((x, y))

    return result

# Размеры изображения
WIDTH, HEIGHT = 10000, 10000

# Создаем пустое изображение
img = Image.new('RGB', (WIDTH, HEIGHT), 'white')
draw = ImageDraw.Draw(img)

# Данные отрезка
x1, y1 = 0, 0
x2, y2 = 113, 140
k=20
# Рисуем отрезок красным цветом
draw.line([(x1, y1), (x2*k, y2*k)], fill='red', width=1)

# Сохраняем изображение
img.save('segment_drawn.png')

# Загружаем изображение обратно
img = Image.open('segment_drawn.png')

# Извлекаем красные точки
red_points = extract_red_pixels(img)

# Выводим результат
print((red_points), "целочисленных точек найдено.")


# # Пример использования
# x1, y1 = 0, 0
# x2, y2 = 113, 140
# xc, yc = 101, 82
#
# result = is_point_on_segment(x1, y1, x2, y2, xc, yc)
# print(result)
# a = [(x, y) for x in range(x1, x2 + 1) for y in range(y1, y2 + 1)]
#
# for xc, yc in a:
#     if is_point_on_segment(x1, y1, x2, y2, xc, yc)<1e-9:
#         print((xc, yc), "Точка лежит на отрезке.")
# #
#
#
# for xc, yc in a:
#     if is_point_on_segment(x1, y1, x2, y2, xc, yc):
#         print((xc, yc), "Точка лежит на отрезке.")
