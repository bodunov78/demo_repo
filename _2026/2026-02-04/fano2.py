from collections import Counter

word = "КОЛОБОК"
freq = Counter(word)  # {'О': 3, 'К': 2, 'Л': 1, 'Б': 1}
print (freq)
known = {'А': '001', 'И': '01', 'С': '10'}
used_codes = set(known.values())

# Начинаем с доступных префиксов после построения дерева от известных кодов
# Минимальные коды для новых букв: 11 (длина 2), затем 000, 011, 100, 101, 110, 111 (длина 3)
available = ['11', '000', '011', '100', '101', '110', '111']
letter_codes = known.copy()

# Присваиваем самые короткие доступные коды самым частым буквам
sorted_letters = sorted([c for c in freq if c not in letter_codes], key=lambda x: -freq[x])
for i, letter in enumerate(sorted_letters):
    letter_codes[letter] = available[i]

# Считаем длину кодирования слова
total_len = sum(len(letter_codes[ch]) for ch in word)
print(total_len)