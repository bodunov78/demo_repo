#Текстовый файл 0.txt состоит не более чем из 106 символов
# и содержит только заглавные буквы латинского алфавита (A..Z).
# Определите максимальное количество идущих подряд символов,
# среди которых нет символов Q или W.

with open("0.txt") as f:
    s=f.readline()
    s=s.strip()
    s=s.replace('Q',':').replace('W',':')
    a=s.split(':')
    m=[(len(x),x) for x in a]
    print (max(m))
    print (len(max( a,key=len)))
    print (max(a,key=len))
    