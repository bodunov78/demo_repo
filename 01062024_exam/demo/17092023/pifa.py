# 1 найти 100 первых пифогорейских троек из натуральных (a,b,c) так что (a*a+b*b=c*c) результат вывести на экран
# 2.найти хотябы одну тройку целых чисел (a,b,c) удовлетворяющую равенству a*a*a+b*b*b=c*c*c
# 3.написать программу используя метод Ньютона по извленению квадратного корня из трехзначного числа с точностью до 0,01
# https://cf.ppt-online.org/files/slide/z/Z67xrHzkmNSURMonF5if2Q3cDBEvyW9bapGeYl/slide-29.jpg


def fu11():
    i = 0
    cnt = 0
    for a in range(1, 323):
        for b in range(1, 323):
            for c in range(1, 323):
                i += 1
                if a ** 2 + b ** 2 == c ** 2 and cnt < 100:
                    cnt += 1
                    print(a, b, c, cnt)
    print(i)


def fu12():
    i = 0
    cnt = 0
    for a in range(1, 323):
        for b in range(1, 323):
            for c in range(1, 323):
                i += 1
                if a ** 2 + b ** 2 == c ** 2 and a < b < c and cnt < 100:
                    cnt += 1
                    print(a, b, c, cnt)
    print(i)


def fu13():
    i = 0
    cnt = 0
    for a in range(1, 323):
        for b in range(1, 323):
            for c in range(1, 323):
                i += 1
                if a ** 2 + b ** 2 == c ** 2 and a < b < c and cnt <= 100:
                    cnt += 1
                    print(a, b, c, cnt)
                elif cnt > 100:
                    print(i)
                    return (i)


def fu14():
    i = 0
    cnt = 0
    for a in range(1, 323):
        for b in range(a + 1, 323):
            for c in range(b + 1, 323):
                i += 1
                if a ** 2 + b ** 2 == c ** 2 and a < b < c and cnt < 100:
                    cnt += 1
                    print(a, b, c, cnt)
                elif cnt >= 100:
                    print(i)
                    return (i)


def fu15():
    i = 0
    cnt = 0
    for a in range(1, 323):
        for b in range(a + 1, 323):
            for c in range(b + 1, 323):
                i += 1
                if a ** 2 + b ** 2 == c ** 2 and a < b < c and cnt < 100:
                    cnt += 1
                    print(a, b, c, cnt)
                    break
                elif cnt >= 100:
                    print(i)
                    return (i)


def fu16():
    i = 0
    cnt = 0
    a = 0
    while cnt < 100 and a < 323:
        a += 1
        b = a
        while cnt < 100 and b < 323:
            b += 1
            c = b
            while cnt < 100 and c < 323:
                c += 1
                i += 1
                if a ** 2 + b ** 2 == c ** 2:
                    cnt += 1
                    print(a, b, c, cnt)
                    break
                elif a ** 2 + b ** 2 < c ** 2:
                    break

    print(i)


def fu17():
    i = 0
    cnt = 0
    a = 0
    maxi = 0
    while cnt < 100:
        a += 1
        b = a
        while cnt < 100 and b < 323:  # 1201
            b += 1
            c = b
            while cnt < 100 and a ** 2 + b ** 2 >= c ** 2:
                c += 1
                i += 1
                if a ** 2 + b ** 2 == c ** 2:
                    cnt += 1
                    print(a, b, c, cnt)
                    # maxi = max(maxi, b)
                    break
                # elif a ** 2 + b ** 2 < c ** 2:
                #     break

    print(i, maxi)


def fu18():
    i = 0
    cnt = 0
    a = 0
    maxi = 0
    while cnt < 100:
        a += 1
        b = a
        while cnt < 100 and b < 323:  # 1201
            b += 1
            c = b + a % 2
            while cnt < 100 and a ** 2 + b ** 2 >= c ** 2:

                i += 1
                if a ** 2 + b ** 2 == c ** 2:
                    cnt += 1
                    print(a, b, c, cnt)
                    # maxi = max(maxi, b)
                    break
                # elif a ** 2 + b ** 2 < c ** 2:
                #     break
                c += 2
    print(i, maxi)

# 2.найти хотябы одну тройку целых чисел (a,b,c) удовлетворяющую равенству a*a*a+b*b*b=c*c*c
def fu20():
    i = 0
    cnt = 0
    for a in range(-100, 100):
        for b in range(-100, 100):
            for c in range(-100, 100):
                i += 1
                if a ** 3 + b ** 3 == c ** 3 :
                    print(a, b, c, cnt)
                    return 1

# 3.написать программу используя метод Ньютона по извленению квадратного корня из трехзначного числа с точностью до 0,01
# https://cf.ppt-online.org/files/slide/z/Z67xrHzkmNSURMonF5if2Q3cDBEvyW9bapGeYl/slide-29.jpg

def fu30():
    x=int (input("Введи трехзначное число:"))
    if 100<=x<=999:
        x1=x//2
        while abs(x-x1**2) >=0.01:
            x1=(x1+x/x1)/2
            print(x1)
        else:
            print(f"корен из {x} c  точностью 0.01 равен {x1},квадрат корня {x1**2}")

# fu10()
# fu11()
# fu12()
# fu13()
# fu14()
# fu15()
# fu16()
# fu17()
# fu18()

fu30()
