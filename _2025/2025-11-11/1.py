#https://math-ege.sdamgia.ru/problem?id=563555
#Даны три различных натуральных числа такие, что второе число равно сумме цифр первого, а третье— сумме цифр второго.
#а)Может ли сумма трех чисел быть равной 420?
#б)Может ли сумма трех чисел быть равной 419?
#в)Сколько существует троек чисел, таких что: первое число— трехзначное, а последнее равно 5?


# найти сумму цифр
def f(n):
    suma=0
    while n>0:
        ost=n%10
        suma+=ost
        n=n//10
    return suma

#a
for a in range(100,999+1):
    b=f(a)
    c=f(b)
    if c<b<a and (a+b+c)==420:
        print ("#A",a)
#b
for a in range(100,999+1):
    b=f(a)
    c=f(b)
    if c<b<a and (a+b+c)==419:
        print ("#B",a)

#c
cnt=0
for a in range(100,999+1):
    b=f(a)
    c=f(b)
    if c<b<a and c==5:
        cnt+=1
        print ("#C",a,cnt)
