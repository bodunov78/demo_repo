def f(s):
    m=c=0
    for i in s:
        if i.upper()!='Z':
            c+=1
            m=max(m,c)
        else:
            c=0
    return m
print(f(input("Строка: ")))
