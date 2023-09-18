def fu():
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


def fu0():
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


def fu1():
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


def fu2():
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


def fu3():
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


def fu4():
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


def fu5():
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


def fu6():
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


# fu()
# fu0()
# fu1()
# fu2()
# fu3()
# fu4()
fu5()
fu6()
