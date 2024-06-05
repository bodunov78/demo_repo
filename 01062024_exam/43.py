# # 15 на отрезки
# from itertools import *
#
#
# def f(x):
#     P = 5 <= x <= 100
#     Q = 15 <= x <= 25
#     R = 35 <= x <= 50
#     A = a <= x <= b
#     return (P <= Q) or ((not A) <= R)
#
#
# Ox = [i / 2 for i in range(0 * 2, 150 * 2 + 1)]
#
# array_lines = []
#
# for a, b in combinations(Ox, 2):
#     if all(f(x) == True for x in Ox):
#         array_lines.append(b - a)
#
# print(min(array_lines))
#



























# # 17 задания с тройками чисел
#
# f = open('17_4.txt')
# a = [int(x) for x in f]
# cnt = 0
# min_sum = 10 ** 10
# maxel = -10 ** 9
# for i in range(len(a)):
#     if abs(a[i]) % 100 == 15:
#         maxel = max(a[i], maxel)
#
# for j in range(len(a) - 2):
#     # x = a[j]
#     # y = a[j + 1]
#     # z = a[j + 2]
#     s = [a[j], a[j + 1], a[j + 2]]
#     # if (1000<= abs(s[0]) <= 9999) or (1000<= abs(s[1]) <= 9999) or (1000<= abs(s[2]) <= 9999):
#     count4 = 0
#     for elem in s:
#         if 1000 <= abs(elem) <= 9999:
#             count4 += 1
#
#     summa = sum(s)
#     if count4 == 1 and summa < maxel:
#         min_sum = min(min_sum, summa)
#         cnt += 1
#
# print(cnt, min_sum)
#
#
#






























# def get_good_trika(troika):
#     count_5 = 0  # кол-во чисел в тройке оканчивающихся на 5
#     for j in range(len(troika)):
#         if abs(troika[j]) % 10 == 5:
#             count_5 += 1
#     return count_5
#
#
# a = [int(x) for x in open('17 15.txt')]
# max_element = max([int(a[x]) for x in range(len(a)) if 99 < abs(int(a[x])) <= 1000 and abs(int(a[x])) % 10 == 5])
# count = 0
# max_summ = (-10) ** 9
#
# for i in range(len(a) - 2):
#     troika = [a[i], a[i + 1], a[i + 2]]
#     summa_troika = sum(troika)
#
#     if get_good_trika(troika) == 1:
#         if summa_troika <= max_element:
#             count += 1
#             max_summ = max(max_summ, summa_troika)
#
# print(count, max_summ)
#
#





























# # номер 14 с основанием > 36
# for x in range(0,37):
#       s = ((1*37**3 + 2*37**2 + 3*4**1 + 4*37**0) + (1*37**3 + 2*37**2 + 3*37**1 + 4*37**0)) :
#       if s % 36 == 0:
#            print(x, s // 36)