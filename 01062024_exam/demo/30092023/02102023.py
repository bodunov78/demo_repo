# 1 посчитать количество четных и нечетных числел в массиве
# 2 найти минимальные и максимальные элементы массива
# 3 вывести два максимальных и два минимальных значения массива
# 4  найти сколько чисел в интервале 999 до 2357 при делении на 7 будут иметь остаток от деления 0 1 2 3 4 5 6


# 1 посчитать количество четных и нечетных числел в массиве
def fu11():
    ch,nch=0,0

    # заполняем массив
    arr = [i for i in range(199) if i % 3 == 0 or i % 4 == 0]
    print(arr)

    for x in arr:
        if x % 2 == 0:
            ch += 1
        else:
            nch += 1


    print (ch,nch)
def fu12():
    ch = 0

    # заполняем массив
    arr = [i for i in range(199) if i % 3 == 0 or i % 4 == 0]
    print(arr)

    for x in arr:
        if x % 2 == 0:
            ch += 1


    print (ch,len(arr)-ch)

def fu13():
    ch = [0]*2

    # заполняем массив
    arr = [i for i in range(199) if i % 3 == 0 or i % 4 == 0]
    for i in arr:
        ch[i%2]+=1

    print(f"четных {ch[0]}, нечетных {ch[1]}")


# 2 найти минимальные и максимальные элементы массива

def fu21():
    ch = [0]*2
    maxi=-1*10**20
    mini=10**20
    # заполняем массив
    arr = [i for i in range(199) if i % 3 == 0 or i % 4 == 0]
    for i in arr:
            if i < mini:
                mini=i
            if i>maxi:
                maxi=i
    print(f"Максимальный {maxi}, минимальный {mini}")


def fu22():
    ch = [0]*2
    maxi=-1*10**20
    mini=10**20
    # заполняем массив
    arr = [i for i in range(199) if i % 3 == 0 or i % 4 == 0]
    for i in arr:
            mini=min(mini,i)
            maxi = max(maxi, i)

    print(f"Максимальный {maxi}, минимальный {mini}")

def fu23():
    ch = [0]*2
    maxi=-1*10**20
    mini=10**20
    # заполняем массив
    arr = [i for i in range(199) if i % 3 == 0 or i % 4 == 0]

    print(f"Максимальный {max(arr)}, минимальный {min(arr)}")

# 3 вывести два максимальных и два минимальных значения массива

def fu31():
    ch = [0]*2
    maxi1=-1*10**20
    mini1=10**20
    # заполняем массив
    arr = [i for i in range(199) if i % 3 == 0 or i % 4 == 0]
    arr.sort()

    print(f"1й Максимальный {arr[-1]} , 2й Максимальный {arr[-2]} , 1й минимальный {arr[0]} ,2й минимальный {arr[1]} ")

# 4  найти сколько чисел в интервале 999 до 2357 при делении на 7 будут иметь остаток от деления 0 1 2 3 4 5 6
def fu41():
    ost7 = [0]*7
    for i in range(999,2357+1):
        ost7[i%7]+=1
    print(ost7)

def fu42():
    ost7 = [0]*7

    for i in range(999,2357+1):
        ost7[0]+=1 if i%7==0 else False
        ost7[1] += 1 if i % 7 == 1 else False
        ost7[2] += 1 if i % 7 == 2 else False
        ost7[3] += 1 if i % 7 == 3 else False
        ost7[4] += 1 if i % 7 == 4 else False
        ost7[5] += 1 if i % 7 == 5 else False
        ost7[6] += 1 if i % 7 == 6 else False
    print(ost7)

def fu43():
    ost7 = [0]*7


    for i in range(999,2357+1):
        if i % 7 == 0:
            ost7[0] += 1
        elif i % 7 == 1:
            ost7[1] += 1
        elif i % 7 == 2:
            ost7[2] += 1
        elif i % 7 == 3:
            ost7[3] += 1
        elif i % 7 == 4:
            ost7[4] += 1
        elif i % 7 == 5:
            ost7[5] += 1
        elif i % 7 == 6:
            ost7[6] += 1

    print(ost7)


# fu11()
# fu12()
# fu13()
# fu21()
# fu22()
# fu41()
# fu42()
fu43()
