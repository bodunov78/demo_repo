# Пример бинарного поиска в отсортированном списке
def binary_search(sorted_list, target):
    left = 0
    right = len(sorted_list) -1

    while left <= right:
        mid = (left + right) // 2

        if sorted_list[mid] == target:
            return mid # Элемент найден
        elif sorted_list[mid] < target:
            left = mid + 1 # Ищем в правой половине
        else:
            right = mid - 1 # Ищем в левой половине

    return -1 # Элемент не найден

# Тестируем функцию
numbers = [1, 3, 5, 7, 9, 11, 13, 15, 17]
result = binary_search(numbers, 7)
print(f"Индекс элемента: {result}") # Выведет: Индекс элемента: 3