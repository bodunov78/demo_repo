a=123456
w=''
while a>0:
    if a%30<10:
        w=str(a%30)+w
    else:
        w=chr(ord('A')+a%30-10)+w
    a//=30
print(w)
