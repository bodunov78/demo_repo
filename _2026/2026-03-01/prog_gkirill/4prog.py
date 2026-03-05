ch=123456
x=''
d = "0123456789ABCDEFGHIJKLMNOPQRST"
while ch > 0:
    ost=ch%30
    x = d[ost] + x
    ch = ch// 30

print(x)