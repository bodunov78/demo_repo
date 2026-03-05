ch=127
print(bin(ch)[2:])

print()

x=''
while ch > 0:
    x = str(ch % 2) + x
    ch = ch// 2

print(x)