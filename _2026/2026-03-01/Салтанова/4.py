a=123456
s=''
while a>0:
    if a%30<10:
        s=str(a%30)+s
    else:
        s=chr(ord('A') + a%30-10)+s
    a=a//30
print(s)
