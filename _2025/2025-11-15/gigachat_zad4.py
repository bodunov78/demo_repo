from PIL import  *
from numpy import *

# Исходные данные: заданные коды и подлежащие кодированию буквы
given_codes = {
    'А': '010',  # Зафиксированный код для буквы 'А'
    'Б': '011',  # Зафиксированный код для буквы 'Б'
    'Г': '100'  # Зафиксированный код для буквы 'Г'
}

letters = ['А', 'Б', 'Г', 'И', 'М', 'Р', 'Я']  # Полный список используемых букв


# Функция для проверки префиксного свойства (правила Фано)
def is_valid_code(code_list):
    """
    Эта функция проверяет, соответствует ли полученный список кодов условию Фано.
    Правила Фано запрещают одному коду быть началом другого.
    """
    sorted_codes = sorted(code_list)  # Сортируем коды для упрощенной проверки
    for i in range(len(sorted_codes) - 1):
        prefix = sorted_codes[i]  # Текущий код
        next_code = sorted_codes[i + 1]  # Следующий код
        if next_code.startswith(prefix):  # Если следующий код начинается с текущего
            return False  # Нарушение правила Фано
    return True  # Все коды соответствуют правилу Фано


# Основная логика поиска минимальных кодов
def find_minimal_coding():
    """
    Поиск оптимального набора кодов для оставшихся букв,
    обеспечивающего минимальное количество бит для слова "МАГИЯ",
    с сохранением условия Фано.
    """
    # Определим, какие буквы остались без заданных кодов
    remaining_letters = set(letters) - given_codes.keys()

    # Найдем доступный диапазон бинарных кодов для оставшихся букв
    available_codes = []  # Список доступных кодов
    max_code_length = 3  # Максимально разрешенная длина кода
    for length in range(2, max_code_length + 1):  # Цикл по возможным длинам кодов
        # Создаем бин. представление чисел от 0 до pow(2, length)-1
        for num in range(pow(2, length)):
            binary_representation = format(num, f'{length}b')  # Преобразование числа в бинарный вид
            available_codes.append(binary_representation)

    # Переберем все возможные комбинации свободных кодов
    from itertools import permutations
    possible_combinations = permutations(available_codes, len(remaining_letters))

    best_result = None  # Лучший набор кодов
    min_total_length = float('inf')  # Начальное значение для минимума

    # Проходим по всем возможным комбинациям
    for combination in possible_combinations:
        # Формируем новый словарь кодов
        current_codes = dict(given_codes)
        for letter, code in zip(remaining_letters, combination):
            current_codes[letter] = code

        # Получаем полный список текущих кодов
        all_codes = list(current_codes.values())

        # Проверяем, соответствуют ли коды правилу Фано
        if not is_valid_code(all_codes):
            continue  # Переходим к следующему варианту, если нарушение правила

        # Рассчитываем общую длину для слова "МАГИЯ"
        word = "МАГИЯ"
        total_length = sum(len(current_codes.get(letter)) for letter in word)

        # Обновляем наилучший результат, если нашли короче код
        if total_length < min_total_length:
            min_total_length = total_length
            best_result = current_codes.copy()  # Копируем лучшие коды

    return best_result, min_total_length


# Запускаем основную функцию поиска
best_coding, minimal_length = find_minimal_coding()

# Вывод результатов
if best_coding:
    print("Оптимальные коды:")
    for letter, code in best_coding.items():
        print(f"{letter}: {code}")  # Печать оптимального набора кодов
    print(f"\nМинимальное количество бит для кодирования слова \"МАГИЯ\": {minimal_length}")
else:
    print("Ошибка: не найдено подходящего набора кодов.")