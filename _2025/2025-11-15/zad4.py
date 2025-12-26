
# Используем встроенный модуль itertools для удобного перебора возможных комбинаций

def calculate_minimum_bits(word):
    # Заданные коды
    codes = {
        'А': '010',  # 3 бита
        'Б': '011',  # 3 бита
        'Г': '100'  # 3 бита
    }

    # Слово, которое хотим закодировать
    word_to_encode = list(word)

    total_length = 0

    for char in word_to_encode:
        if char in codes:
            # Если код известен, используем известный код
            code_len = len(codes[char])
        else:
            # Оставшиеся символы будем считать минимальным числом бит
            code_len = 2

        total_length += code_len

    return total_length


word = "МАГИЯ"
min_bits_needed = calculate_minimum_bits(word)
print(f"Наименьшее количество двоичных знаков для кодирования слова '{word}' равно {min_bits_needed}.")
