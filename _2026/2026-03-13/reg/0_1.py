from re import *
for i in range(0,10**9,23):
    # reg=rf"(12345[0-9]7)*)"
    pattern_groups = r'(^12345)(\d?)(7)(\d)(8)$'
    for match in finditer(pattern_groups, str(i)):
        groups = match.groups()
        print(f"Полный номер: {match.group()}")
        print(f"  - Префикс: {groups[0]}")
        print(f"  - Цифра 1: {groups[1] if groups[1] else 'отсутствует'}")
        print(f"  - Семерка: {groups[2]}")
        print(f"  - Цифра 2: {groups[3] if groups[3] else 'отсутствует'}")
        print(f"  - Восьмерка: {groups[4]}")
        print()

