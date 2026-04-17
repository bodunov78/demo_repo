import math
import time


def find_pythagorean_triples(limit):
    """
    Находит все уникальные пифагоровы тройки (a, b, c), где c <= limit.
    Возвращает список троек, отсортированный по гипотенузе (c).
    """
    triples = set()

    # m должно быть больше n. Максимальное m определяется из условия m^2 + n^2 <= limit
    # Грубая оценка: m^2 < limit, так как c = m^2 + n^2 > m^2
    max_m = int(math.sqrt(limit)) + 1

    start_time = time.time()

    for m in range(2, max_m):
        # n должно быть меньше m
        for n in range(1, m):
            # Проверка условий Евклида для примитивной тройки:
            # 1. m и n взаимно просты (gcd = 1)
            # 2. m и n разной четности
            if (m - n) % 2 == 1 and math.gcd(m, n) == 1:
                # Вычисляем примитивную тройку
                a_prim = m * m - n * n
                b_prim = 2 * m * n
                c_prim = m * m + n * n
                # print (a_prim,b_prim,m,n)
                # Убедимся, что a - положительное (a_prim всегда > 0 при m > n)
                # и отсортируем a и b, чтобы (a,b) и (b,a) не дублировались в set
                a_prim, b_prim = sorted([a_prim, b_prim])

                # Умножаем на коэффициент k
                k = 1
                while True:
                    a = a_prim * k
                    b = b_prim * k
                    c = c_prim * k

                    if c > limit:
                        break

                    # Добавляем тройку как кортеж
                    triples.add((a, b, c))
                    k += 1

    end_time = time.time()

    print(f"Поиск завершен за {end_time - start_time:.2f} секунд.")
    print(f"Найдено троек: {len(triples)}")

    # Возвращаем отсортированный список по гипотенузе (c)
    return sorted(list(triples), key=lambda x: x[2])


# Запуск программы
if __name__ == "__main__":
    LIMIT = 1_000_000
    # LIMIT = 1_00

    result = find_pythagorean_triples(LIMIT)

    # Вывод первых 20 троек для примера
    print("\nПервые 20 троек (a, b, c):")
    for i, triple in enumerate(result[:20]):
        print(f"{i + 1}: {triple}")

    # Если нужно сохранить в файл (раскомментируйте при необходимости)
    # with open("pythagorean_triples.txt", "w") as f:
    #     for triple in result:
    #         f.write(f"{triple[0]}, {triple[1]}, {triple[2]}\n")


    # 3 4 5
    # 6 8 10
    # 9 12 15
    # 12 16 20
