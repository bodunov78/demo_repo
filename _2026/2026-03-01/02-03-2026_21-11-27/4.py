n = 123456
s = ''
while n!=0:
    s = str(n % 30) + s
    n = n // 30
print(s)
