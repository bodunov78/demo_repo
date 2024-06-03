#48384 88x4y v 9 + 7x44y v 11  будет наименьшим и кратно 61
for x in '012345678':
    for y in '012345678':
        res = int('88'+ x + '4' + y,9) + int('7'+ x + '44' + y,11)
        if res % 61 == 0:
            print(res // 61)


#48385 8x78y v 13 + 79xy7 v 18
result_search = []
for x in '0123456789ABC':
    for y in '0123456789ABC':
        t = int('8' + x + '78' + y, 13) + int('79' + x + y + '7', 18)
        if t % 9 == 0:
            result_search.append(t)
if result_search:
    print(min(result_search) // 9)

for x in range(0,13+1):
    for y in (0,13+1):
        t=y*13**0+8*13**1+7*13**2+x*13**3+8*13**4 +7*18**0+y*18**1+x*18**2+9*18**3+7*18**4

        if t % 9 == 0:
            result_search.append(t)
if result_search:
    print(min(result_search) // 9)


