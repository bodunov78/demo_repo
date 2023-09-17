def fu0():
    i = 0
    cnt = 0
    for a in range(1, 200):
        for b in range(1, 200):
            for c in range(1, 200):
                i += 1
                if a ** 2 + b ** 2 == c ** 2 and a < b < c and cnt < 100:
                    cnt += 1
                    print(a, b, c, cnt)
    print(i)


def fu1():
    i = 0
    cnt = 0
    for a in range(1, 200):
        for b in range(1, 200):
            for c in range(1, 200):
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
    for a in range(1, 200):
        for b in range(a + 1, 200):
            for c in range(b + 1, 200):
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
    for a in range(1, 200):
        for b in range(a + 1, 200):
            for c in range(b + 1, 200):
                i += 1
                if a ** 2 + b ** 2 == c ** 2 and a < b < c and cnt < 100:
                    cnt += 1
                    print(a, b, c, cnt)
                    break
                elif cnt >= 100:
                    print(i)
                    return (i)


fu0()
fu1()
fu2()
fu3()
