n = 123456
ch = "0123456789ABCDEFGHIJKLMNOPQRST"
res = ""
while n > 0:
    res = ch[n % 30] + res
    n //= 30
print(res)
