b=int("101101",2)/2**2
a=int("246",8)/8**1
print(a+b,type(a+b))
print (hex(int(a+b))[2:])


bit=8
n=-38
x=2**bit-1+n+1
print(x,bin(x)[2:])