from string import *
for x in range(0,11+1):
    a=3*12**0+x*12**1+4*12**2+5*12**3+1*12**4
    b=5*12**0+6*12**1+3*12**2+x*12**3+1*12**4
    if (a+b)%13==0:
        print ((a+b)//13,x)
#
# 1 87654
# 1 00000
#  8 0000
#     7 000
#        6 00
#           5 0
#              4


for x in range(0,11+1):
    a=int("15400",12)+int("3",12) +x*12**1
    b=int("10000",12)+x*12**3+int("365",12)
    if (a+b)%13==0:
        print ((a+b)//13,x)

for x in "0123456789ab":
    a=int(f"154{x}3",12)
    b=int(f"1{x}365",12)
    if (a+b)%13==0:
        print ((a+b)//13,x)

for x in printable[:12]:
    a=int(f"154{x}3",12)
    b=int(f"1{x}365",12)
    if (a+b)%13==0:
        print ((a+b)//13,x)

# print (printable)
# 2ABx_12+x8E_17.

for x in printable[:12]:
    a=int(f"12ab{x}",12)
    b=int(f"{x}8e",17)
    if (a+b)%27==0:
        print (x,(a+b)//27)
mina=[]
for x in printable[:13]:
    for y in printable[:13]:
        a = int(f"8{x}78{y}", 13)
        b = int(f"79{x}{y}7", 18)
        if (a + b) % 9 == 0:
            mina.append((a + b) // 9)
            print(x,y, (a + b) // 9)

print (min(mina))