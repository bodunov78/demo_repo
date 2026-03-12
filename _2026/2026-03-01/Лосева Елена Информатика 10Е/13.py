#13.Написать функцию, возвращающую НОД и НОК двух чисел
"""
#Нод
a=int(input())
b=int(input())
while a!=0 and b!=0:
    if a>b:
        a=a%b
    else:
        b=b%a
print(a+b)

"""
#Нок
a=int(input())
b=int(input())
i=min(a,b)
while True:
    if i%a==0 and i%b==0:
        break
    i+=1
print(i)
