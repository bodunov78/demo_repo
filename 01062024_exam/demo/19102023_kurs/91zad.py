# прочитать csv и засунуть в массив
# ип 9
# 57416
# i
# Откройте файл электронной таблицы, содержащей в каждой строке пять натуральных чисел. Определите количество строк таблицы, содержащих числа, для которых выполнены оба условия:
#
# — в строке все числа различны;
#
# — удвоенная сумма максимального и минимального чисел строки не больше суммы оставшихся трёх её чисел.
#
# В ответе запишите только число.
file=open("1_9.csv","r")


cnt=0
with open("1_9.csv") as file:
    for x in file:
        a=list(map(int,x.split(';')))
        if len(a) == len(set(a)):

            a.sort()
            if (a[0]+a[-1])*2 <= sum(a)-a[0]-a[-1]:
                cnt += 1
                print(a)

print(cnt)


k=('4','5')
l=('4')
c=(k&l)
print (c)