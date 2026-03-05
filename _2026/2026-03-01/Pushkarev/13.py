print("НОД:")
a,b=int(input()), int(input())
while a!=b:
    if a>b:
        a=a-b
    else:
        b=b-a
print(a)

print()

print("НОК:")
a,b=int(input()), int(input())
m=max(a,b)
while True:
    if m%a==0 and m%b==0:
        print(m)
        break
    else:
        m+=1
